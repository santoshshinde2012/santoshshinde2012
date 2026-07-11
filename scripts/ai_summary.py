#!/usr/bin/env python3
"""Regenerate the "What I'm Shipping Lately" README section.

Pulls recent public GitHub activity, asks an LLM (GitHub Models — no external
API key, just the Actions GITHUB_TOKEN) to write a short, human summary, and
injects it between the AI-SUMMARY markers. If the model call fails for any
reason, it falls back to a clean deterministic summary so the section never
breaks. The workflow that itself writes part of this profile is the point:
it demonstrates an agentic, self-updating pipeline rather than describing one.

Env:
  GH_USER            GitHub username (default: santoshshinde2012)
  GITHUB_TOKEN       token used for both the GitHub API and GitHub Models
  MODELS_ENDPOINT    OpenAI-compatible chat endpoint (default: GitHub Models)
  MODELS_MODEL       model id (default: gpt-4o-mini)
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
ENDPOINT = os.getenv(
    "MODELS_ENDPOINT", "https://models.inference.ai.azure.com/chat/completions"
)
MODEL = os.getenv("MODELS_MODEL", "gpt-4o-mini")
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- AI-SUMMARY:START -->", "<!-- AI-SUMMARY:END -->"
WINDOW_DAYS = 21


def _get(url: str) -> list | dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER, "Accept": "application/vnd.github+json"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def recent_activity() -> "OrderedDict[str, list[str]]":
    """repo -> list of recent commit messages / actions."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=WINDOW_DAYS)
    repos: "OrderedDict[str, list[str]]" = OrderedDict()
    try:
        events = _get(f"https://api.github.com/users/{USER}/events/public?per_page=100")
    except (urllib.error.URLError, ValueError):
        return repos
    for ev in events:
        try:
            when = datetime.fromisoformat(ev["created_at"].replace("Z", "+00:00"))
        except (KeyError, ValueError):
            continue
        if when < cutoff:
            continue
        repo = ev.get("repo", {}).get("name", "").split("/")[-1]
        if not repo:
            continue
        bucket = repos.setdefault(repo, [])
        if ev.get("type") == "PushEvent":
            for c in ev.get("payload", {}).get("commits", []):
                msg = c.get("message", "").splitlines()[0].strip()
                if msg and not msg.lower().startswith(("merge", "chore: update readme")):
                    bucket.append(msg)
        elif ev.get("type") == "CreateEvent" and ev.get("payload", {}).get("ref_type") == "repository":
            bucket.append("created the repository")
        elif ev.get("type") == "PullRequestEvent" and ev.get("payload", {}).get("action") == "opened":
            title = ev.get("payload", {}).get("pull_request", {}).get("title")
            if title:
                bucket.append(f"opened PR: {title}")
    # trim
    return OrderedDict((r, msgs[:6]) for r, msgs in repos.items() if msgs)


def digest(activity: "OrderedDict[str, list[str]]") -> str:
    return "\n".join(
        f"- {repo}: " + "; ".join(msgs) for repo, msgs in list(activity.items())[:8]
    )


def llm_summary(text: str) -> str | None:
    if not TOKEN:
        return None
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
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode())
        return data["choices"][0]["message"]["content"].strip()
    except (urllib.error.URLError, KeyError, ValueError, TimeoutError):
        return None


def fallback_summary(activity: "OrderedDict[str, list[str]]") -> str:
    if not activity:
        return "Actively building production LLM systems — agents, RAG pipelines, evals, and data platforms."
    repos = list(activity.keys())[:4]
    lead = ", ".join(f"[`{r}`](https://github.com/{USER}/{r})" for r in repos)
    return f"Recent focus across {lead} — shipping AI/ML systems, agent tooling, and data-platform work."


def render(summary: str) -> str:
    stamp = os.getenv("RUN_DATE", datetime.now(timezone.utc).strftime("%b %d, %Y"))
    return (
        f"{START}\n"
        f"{summary}\n\n"
        f"<sub>Auto-generated from my recent GitHub activity by a GitHub Actions + "
        f"GitHub Models workflow · updated {stamp}</sub>\n"
        f"{END}"
    )


def main() -> None:
    activity = recent_activity()
    summary = llm_summary(digest(activity)) or fallback_summary(activity)
    text = README.read_text()
    block = render(summary)
    if START in text and END in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    else:
        raise SystemExit("AI-SUMMARY markers not found in README.md")
    README.write_text(text)
    print("updated README AI summary:\n", summary)


if __name__ == "__main__":
    main()
