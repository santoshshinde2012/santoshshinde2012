#!/usr/bin/env python3
"""Regenerate the "What I'm Shipping Lately" README section.

Pulls recent public GitHub activity, summarises what's been shipped, and injects
it between the AI-SUMMARY markers. The section is always regenerated from real
activity; whether a model writes the prose depends on configuration.

NOTE: GitHub Models was fully retired on 2026-07-30 (inference API, catalog and
BYOK all removed), so the original "free inference off GITHUB_TOKEN" design no
longer has a backend. This script is now provider-agnostic: point
MODELS_ENDPOINT at any OpenAI-compatible chat endpoint and supply
MODELS_API_KEY, and the prose is model-written. With no key configured it
degrades to a deterministic summary built from the same activity data.

The footnote it renders always states which path actually ran, so the README can
never advertise a model-written line that a template in fact produced. If a key
IS configured and the call fails, the job exits non-zero rather than silently
downgrading — a broken pipeline should be visible, not papered over.

Env:
  GH_USER            GitHub username (default: santoshshinde2012)
  GITHUB_TOKEN       token for the GitHub activity API
  MODELS_ENDPOINT    OpenAI-compatible chat completions URL (optional)
  MODELS_API_KEY     bearer token for that endpoint (optional; enables prose)
  MODELS_MODEL       model id for that endpoint
"""
from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from collections import OrderedDict
from datetime import datetime, timedelta, timezone
from pathlib import Path

USER = os.getenv("GH_USER", "santoshshinde2012")
TOKEN = os.getenv("GITHUB_TOKEN", "")
ENDPOINT = os.getenv("MODELS_ENDPOINT", "")
MODELS_KEY = os.getenv("MODELS_API_KEY", "")
MODEL = os.getenv("MODELS_MODEL", "")
# Model-written prose is opt-in: it needs somewhere to send the request and a
# credential for it. Absent either, the deterministic path runs and says so.
LLM_ENABLED = bool(ENDPOINT and MODELS_KEY and MODEL)
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- AI-SUMMARY:START -->", "<!-- AI-SUMMARY:END -->"
WINDOW_DAYS = 21


def _get(url: str) -> list | dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER, "Accept": "application/vnd.github+json"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


SKIP_PREFIXES = (
    "merge",
    "chore: update readme",
    "chore: refresh shipping summary",
    "chore: refresh ai-generated",
)
# Subjects that describe nothing. Surfacing "update" on a profile is worse than
# surfacing nothing, so these are dropped before a headline is chosen.
LOW_SIGNAL = re.compile(
    r"^(wip|tmp|temp|test|minor|small)\b"
    r"|^(fix(ed|es)?|update[ds]?|change[ds]?|tweak(ed)?|clean(ed)? ?up|revert)"
    r"(\s+(the|a|some|few|it|this|that|stuff|things?|docs?|documents?|typos?|"
    r"formatting|lint|readme|files?))*[.!]?$",
    re.I,
)
MAX_REPOS = 6


def _pushed_repos(cutoff: datetime) -> list[str]:
    """Distinct "owner/repo" pushed to inside the window, most recent first.

    Only the event's repo name is used. PushEvent payloads no longer carry a
    `commits` array (they are now just before/head/push_id/ref/repository_id),
    so commit messages have to come from the commits API instead.
    """
    seen: "OrderedDict[str, None]" = OrderedDict()
    for page in (1, 2):
        try:
            events = _get(
                f"https://api.github.com/users/{USER}/events/public"
                f"?per_page=100&page={page}"
            )
        except (urllib.error.URLError, ValueError):
            break
        if not events:
            break
        for ev in events:
            try:
                when = datetime.fromisoformat(ev["created_at"].replace("Z", "+00:00"))
            except (KeyError, ValueError):
                continue
            if when < cutoff:
                return list(seen)
            if ev.get("type") != "PushEvent":
                continue
            full = ev.get("repo", {}).get("name", "")
            if full.count("/") == 1:
                seen.setdefault(full, None)
    return list(seen)


def _commits(full_repo: str, cutoff: datetime) -> list[str]:
    """My commit subjects in one repo since the cutoff."""
    since = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        data = _get(
            f"https://api.github.com/repos/{full_repo}/commits"
            f"?author={USER}&since={since}&per_page=20"
        )
    except (urllib.error.URLError, ValueError):
        return []
    out = []
    for c in data if isinstance(data, list) else []:
        msg = (c.get("commit", {}).get("message") or "").splitlines()[0].strip()
        if msg and not msg.lower().startswith(SKIP_PREFIXES) and not LOW_SIGNAL.match(msg):
            out.append(msg)
    return out


def recent_activity() -> "OrderedDict[str, list[str]]":
    """"owner/repo" -> my recent commit subjects there."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=WINDOW_DAYS)
    repos: "OrderedDict[str, list[str]]" = OrderedDict()
    for full in _pushed_repos(cutoff)[:MAX_REPOS]:
        msgs = _commits(full, cutoff)
        if msgs:
            repos[full] = msgs[:6]
    return repos


def digest(activity: "OrderedDict[str, list[str]]") -> str:
    return "\n".join(
        f"- {repo}: " + "; ".join(msgs) for repo, msgs in list(activity.items())[:8]
    )


class ModelError(RuntimeError):
    """The model call failed — surfaced instead of silently swallowed."""


def llm_summary(text: str) -> str:
    if not LLM_ENABLED:
        raise ModelError("MODELS_ENDPOINT / MODELS_API_KEY / MODELS_MODEL not set")
    body = json.dumps(
        {
            "model": MODEL,
            "temperature": 0.4,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You write a GitHub profile section for Santosh Shinde, an AI "
                        "Lead Engineer. From the raw activity log, write 2-3 tight "
                        "sentences on what he's been building lately, emphasizing AI/ML, "
                        "agents, RAG, evals, and data platforms. Concrete and specific; "
                        "no hype, no emojis, no first person, no headings. Plain prose."
                    ),
                },
                {"role": "user", "content": f"Recent activity:\n{text}"},
            ],
        }
    ).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST")
    req.add_header("Authorization", f"Bearer {MODELS_KEY}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:400]
        raise ModelError(f"{ENDPOINT} -> HTTP {e.code}: {detail}") from e
    except (urllib.error.URLError, TimeoutError) as e:
        raise ModelError(f"{ENDPOINT} unreachable: {e}") from e
    try:
        out = data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as e:
        raise ModelError(f"unexpected response shape: {str(data)[:400]}") from e
    if not out:
        raise ModelError("model returned an empty summary")
    return out


def _reads_like_work(msg: str, repo_name: str) -> bool:
    """Is this subject a description of work, or just a label?

    Initial commits are usually the repo's own name ("poc - Churn vs Risk"),
    which says nothing on a profile. Require a few words and some signal that
    the message is about a change rather than a title.
    """
    words = [w for w in re.split(r"[\s\-_]+", msg) if w]
    if len(words) < 4:
        return False
    # "poc - Churn vs Risk" against repo "churn-vs-risk-poc": mostly the name.
    name_parts = {p.lower() for p in re.split(r"[\s\-_]+", repo_name) if p}
    if name_parts:
        overlap = sum(1 for w in words if w.lower() in name_parts)
        if overlap / len(words) > 0.5:
            return False
    return True


def deterministic_summary(activity: "OrderedDict[str, list[str]]") -> str:
    """Concrete and checkable: the repos actually touched, and the real headline
    change in each. No adjectives the activity log doesn't support."""
    if not activity:
        return (
            f"No public pushes in the last {WINDOW_DAYS} days — current work is in "
            "private repositories."
        )
    lines = []
    for full, msgs in list(activity.items())[:5]:
        name = full.split("/")[-1]
        n = len(msgs)
        good = [m for m in msgs if _reads_like_work(m, name)]
        if good:
            # The most *descriptive* subject reads better than the most recent
            # one; prefer the longest that still fits on a line.
            headline = max(good, key=lambda m: (len(m) <= 88, len(m))).rstrip(".")
            if len(headline) > 88:
                headline = headline[:85].rstrip() + "…"
            extra = f" _(+{n - 1} more)_" if n > 1 else ""
            lines.append(f"- **[{name}](https://github.com/{full})** — {headline}{extra}")
        else:
            # Nothing worth quoting — state the volume rather than surface a
            # subject that reads like a repo name.
            lines.append(
                f"- **[{name}](https://github.com/{full})** — "
                f"{n} commit{'s' if n != 1 else ''}"
            )
    return "\n".join(lines)


GANTT_ONGOING = re.compile(
    r"(:\s*(?:active|crit),\s*\w+,\s*\d{4}-\d{2}-\d{2},\s*)(\d{4}-\d{2}-\d{2})"
)


def refresh_timeline(text: str) -> tuple[str, int]:
    """Roll the Gantt's open-ended bars forward to today.

    The chart is titled "2014 to today" but every ongoing bar carried a
    hardcoded end date, so it drifted a little further from the truth every
    week. Only `active` and `crit` rows move; `done` rows are history and
    `milestone` rows carry a `0d` duration, so neither matches.
    """
    today = os.getenv("RUN_DATE_ISO", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    return GANTT_ONGOING.subn(lambda m: m.group(1) + today, text)


def render(summary: str, *, model_written: bool) -> str:
    stamp = os.getenv("RUN_DATE", datetime.now(timezone.utc).strftime("%b %d, %Y"))
    # The footnote states which path produced the text, so the README's
    # "written by a workflow" claim is never stronger than what actually ran.
    provenance = (
        f"Prose written by <code>{MODEL}</code> from my last {WINDOW_DAYS} days "
        "of public GitHub activity"
        if model_written
        else f"Built from my last {WINDOW_DAYS} days of public GitHub activity"
    )
    return (
        f"{START}\n"
        f"{summary}\n\n"
        f"<sub>{provenance} · "
        f"[workflow](.github/workflows/ai-summary.yml) · updated {stamp}</sub>\n"
        f"{END}"
    )


def main() -> None:
    activity = recent_activity()
    if LLM_ENABLED:
        # A configured provider that then fails is a real breakage: fail the job
        # rather than quietly shipping a different kind of summary.
        try:
            summary, model_written = llm_summary(digest(activity)), True
        except ModelError as e:
            raise SystemExit(
                f"::error::model call failed: {e}\nREADME left unchanged. Unset "
                "MODELS_API_KEY to run the deterministic path on purpose."
            ) from e
    else:
        print("::notice::no model provider configured — deterministic summary")
        summary, model_written = deterministic_summary(activity), False
    text = README.read_text()
    text, moved = refresh_timeline(text)
    if moved:
        print(f"::notice::rolled {moved} Gantt bars forward to today")
    block = render(summary, model_written=model_written)
    if START in text and END in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    else:
        raise SystemExit("AI-SUMMARY markers not found in README.md")
    README.write_text(text)
    print("updated README AI summary:\n", summary)


if __name__ == "__main__":
    main()
