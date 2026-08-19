<h1 align="center">Santosh Shinde</h1>

<p align="center">
  <a href="https://www.santoshshinde.com/">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=2F81F7&center=true&vCenter=true&width=620&lines=AI+Engineer+Lead+%40+Syngenta;I+design+%26+ship+production-grade+LLM+systems;Author+of+the+open-source+FrameSleuth+agent;AI+that+ships." alt="Santosh Shinde — AI Engineer Lead at Syngenta" />
  </a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/shindesantosh">
    <!-- Inline logo: simple-icons dropped LinkedIn's mark, so `logo=linkedin` renders text-only. -->
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMC40NDcgMjAuNDUyaC0zLjU1NHYtNS41NjljMC0xLjMyOC0uMDI3LTMuMDM3LTEuODUyLTMuMDM3LTEuODUzIDAtMi4xMzYgMS40NDUtMi4xMzYgMi45Mzl2NS42NjdIOS4zNTFWOWgzLjQxNHYxLjU2MWguMDQ2Yy40NzctLjkgMS42MzctMS44NSAzLjM3LTEuODUgMy42MDEgMCA0LjI2NyAyLjM3IDQuMjY3IDUuNDU1djYuMjg2ek01LjMzNyA3LjQzM2MtMS4xNDQgMC0yLjA2My0uOTI2LTIuMDYzLTIuMDY1IDAtMS4xMzguOTItMi4wNjMgMi4wNjMtMi4wNjMgMS4xNCAwIDIuMDY0LjkyNSAyLjA2NCAyLjA2MyAwIDEuMTM5LS45MjUgMi4wNjUtMi4wNjQgMi4wNjV6bTEuNzgyIDEzLjAxOUgzLjU1NVY5aDMuNTY0djExLjQ1MnpNMjIuMjI1IDBIMS43NzFDLjc5MiAwIDAgLjc3NCAwIDEuNzI5djIwLjU0MkMwIDIzLjIyNy43OTIgMjQgMS43NzEgMjRoMjAuNDUxQzIzLjIgMjQgMjQgMjMuMjI3IDI0IDIyLjI3MVYxLjcyOUMyNCAuNzc0IDIzLjIgMCAyMi4yMjUgMHoiLz48L3N2Zz4%3D" alt="LinkedIn" />
  </a>
  <a href="https://medium.com/@santosh-shinde">
    <img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="https://aithatship.substack.com/">
    <img src="https://img.shields.io/badge/AI%20That%20Ships-FF6719?style=for-the-badge&logo=substack&logoColor=white" alt="AI That Ships on Substack" />
  </a>
  <a href="https://x.com/sanshinde2012">
    <img src="https://img.shields.io/badge/@sanshinde2012-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" />
  </a>
  <a href="https://www.santoshshinde.com/">
    <img src="https://img.shields.io/badge/Portfolio-2F81F7?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Portfolio" />
  </a>
</p>

<br />

<table border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td width="32%" align="center" valign="middle">
      <img src="./assets/profile.svg" width="250" alt="Santosh Shinde" />
    </td>
    <td width="68%" valign="middle">
      <p>I'm an <b>AI Engineer Lead at Syngenta</b>, based in Pune. I design and ship LLM-powered products — RAG pipelines, evaluation loops, and the MLOps plumbing that keeps them running in production.</p>
      <p>My focus is <b>AI/ML — powered by deep full-stack engineering roots</b>. That combination lets me bridge the gap between a working model and a product people can actually rely on.</p>
      <p><i>The model is the easy part. The hard part is everything around it — retrieval, evals, failure modes, cost, and the team that maintains it six months from now. That's what I write about.</i></p>
    </td>
  </tr>
</table>

---

## Proof, Not Claims

I'd rather show working systems than list skills. Everything here runs and is inspectable — the eval scores below are re-measured and republished by CI on every push, not typed in by hand:

| Working system | What it demonstrates | Source |
| --- | --- | --- |
| **FrameSleuth agent** | The open-source MCP server behind [FrameSleuth](https://www.framesleuth.com/) — local video → structured Context Bundle, no frames leaving the machine. I wrote the initial commit and most of what followed. | [repo](https://github.com/thestackhub1/framesleuth-agent) · [site](https://www.framesleuth.com/) |
| **ask-santosh** | Retrieval-augmented Q&A over my writing, gated in CI two ways: a **key-free retrieval gate** (recall@k · MRR over a labelled corpus) that runs on every push, and a **DeepEval** answer suite (faithfulness · answer-relevancy · contextual-relevancy) when a judge key is configured. | [repo](https://github.com/santoshshinde2012/ask-santosh) · [gate](https://github.com/santoshshinde2012/ask-santosh/blob/main/evals/test_retrieval.py)<br/><a href="https://raw.githubusercontent.com/santoshshinde2012/ask-santosh/gh-pages/metrics/summary.json"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/santoshshinde2012/ask-santosh/gh-pages/metrics/recall3.json" alt="recall@3" /></a> <a href="https://raw.githubusercontent.com/santoshshinde2012/ask-santosh/gh-pages/metrics/summary.json"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/santoshshinde2012/ask-santosh/gh-pages/metrics/mrr.json" alt="MRR" /></a> <a href="https://raw.githubusercontent.com/santoshshinde2012/ask-santosh/gh-pages/metrics/summary.json"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/santoshshinde2012/ask-santosh/gh-pages/metrics/updated.json" alt="last measured" /></a> |
| **Multi-agent on Databricks** | Production multi-agent orchestration, beyond Genie code | [repo](https://github.com/santoshshinde2012/multi-agent-sales-ops-tpch-databricks) · [write-up](https://medium.com/data-science-collective/beyond-genie-code-orchestrating-production-multi-agent-systems-on-databricks-86ac51e9c55b) |
| **This profile** | The section below is regenerated weekly from my real GitHub activity by a scheduled workflow. Its footnote states how each run was produced, so the claim can't drift from what actually ran. | [workflow](.github/workflows/ai-summary.yml) · [script](scripts/ai_summary.py) |

---

## What I'm Shipping Lately

<!-- AI-SUMMARY:START -->
- **[santoshshinde2012](https://github.com/santoshshinde2012/santoshshinde2012)** — docs(readme): correct FrameSleuth credit, refresh stale content _(+5 more)_
- **[crop-disease-prediction](https://github.com/santoshshinde2012/crop-disease-prediction)** — chore: add Apache-2.0 LICENSE _(+1 more)_
- **[ask-santosh](https://github.com/santoshshinde2012/ask-santosh)** — feat(evals): add a key-free retrieval gate that actually runs _(+2 more)_
- **[multi-agent-sales-ops-tpch-databricks](https://github.com/santoshshinde2012/multi-agent-sales-ops-tpch-databricks)** — fix: declare Python 3.11, which the code has always required _(+2 more)_
- **[node-ts-sequelize-pg-boilerplate](https://github.com/santoshshinde2012/node-ts-sequelize-pg-boilerplate)** — fix: remove Code Climate badges showing another repo's scores

<sub>Built from my last 21 days of public GitHub activity · [workflow](.github/workflows/ai-summary.yml) · updated Aug 19, 2026</sub>
<!-- AI-SUMMARY:END -->

---

## What I'm Building — FrameSleuth

> ### *"Turn any video into code your agent can ship."*

**[FrameSleuth](https://www.framesleuth.com/)** is a local-first AI system that converts screen recordings into structured, evidence-cited context bundles for coding agents. Record a bug or a feature demo — it reads every frame, transcribes the narration, and captures console and network activity, then hands your agent repro steps, error evidence, and code candidates it can act on.

I build and maintain **[`framesleuth-agent`](https://github.com/thestackhub1/framesleuth-agent)** — the open-source Python MCP server underneath it. Local video in, structured Context Bundle out, over MCP. It's public, so you can read the pipeline rather than take my word for it: keyframe extraction, transcript alignment, bundle contract, Docker image built from a pinned lockfile in CI.

<p align="center">
  <a href="https://github.com/thestackhub1/framesleuth-agent"><img src="https://img.shields.io/badge/source-framesleuth--agent-2F81F7?style=flat-square&logo=github&logoColor=white" alt="framesleuth-agent source" /></a>
  <a href="https://github.com/thestackhub1/framesleuth-agent"><img src="https://img.shields.io/github/stars/thestackhub1/framesleuth-agent?style=flat-square&color=D97706&logo=github&logoColor=white" alt="Stars" /></a>
  <img src="https://img.shields.io/badge/Local--first-16A34A?style=flat-square&logoColor=white" alt="Local-first" />
  <img src="https://img.shields.io/badge/MCP-000000?style=flat-square&logo=modelcontextprotocol&logoColor=white" alt="MCP" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <a href="https://www.framesleuth.com/"><img src="https://img.shields.io/badge/framesleuth.com-2F81F7?style=flat-square&logo=googlechrome&logoColor=white" alt="framesleuth.com" /></a>
</p>

---

## How I Think About the Work

- **End-to-end systems** — not the model in isolation, the full pipeline. Most of the value (and most of the bugs) live between the boxes on the architecture diagram.
- **Tradeoffs that matter to the business** — Lakebase vs Lakehouse, batch vs streaming, RAG vs fine-tuning. These show up in latency, cost, and risk — not just engineering preference.
- **The unglamorous production work** — eval harnesses, observability for non-deterministic systems, drift, and guardrails. The stuff that separates a demo from something you can trust on a Tuesday morning.

---

## What I Keep Running

Shipping something is one thing. Keeping it working for five years, while people
build on it, is a different discipline — and it's the half of "Lead" that a commit
graph doesn't show.

<p>
  <a href="https://github.com/santoshshinde2012/node-boilerplate"><img src="https://img.shields.io/github/stars/santoshshinde2012/node-boilerplate?style=flat-square&label=node-boilerplate&color=D97706&logo=github&logoColor=white" alt="node-boilerplate stars" /></a>
  <img src="https://img.shields.io/github/forks/santoshshinde2012/node-boilerplate?style=flat-square&color=2F81F7&logo=github&logoColor=white" alt="forks" />
  <img src="https://img.shields.io/github/commit-activity/t/santoshshinde2012/node-boilerplate?style=flat-square&color=238636&label=commits" alt="total commits" />
  <img src="https://img.shields.io/github/created-at/santoshshinde2012/node-boilerplate?style=flat-square&color=8B949E&label=maintained%20since" alt="created" />
</p>

- **Five years of upkeep, not a weekend project.** `node-boilerplate` has been
  maintained since March 2021 and is still on a current Node CI matrix, wired to
  SonarCloud, Snyk, CodeQL and njsscan. 82 forks depend on it staying correct.
- **Dependencies stay current.** 274 merged upgrade and security PRs — almost all
  automated, which is the point: the pipeline does the work and I keep it unblocked.
- **Breadth across a team, not one repo.** Beyond my own projects I contribute
  across [`thestackhub1`](https://github.com/thestackhub1) — the FrameSleuth agent,
  a voice agent, a logistics platform, and the web surfaces around them.

<sub>Being straight about the limits: this is sustained maintenance and dependency
discipline, not a large contributor community. One external contributor, three
issues ever. The reviewing half of leading happens in private repos at work, where
a public graph can't see it.</sub>

---

## My Engineering Journey

> A decade of building — from data pipelines and full-stack apps to production AI, with a habit of sharing what I learn along the way.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Fira Code, monospace','taskBkgColor':'#1F6FEB','taskBorderColor':'#2F81F7','activeTaskBkgColor':'#2F81F7','activeTaskBorderColor':'#58A6FF','doneTaskBkgColor':'#8B949E','doneTaskBorderColor':'#6E7681','critBkgColor':'#D97706','critBorderColor':'#B45309','critTextColor':'#ffffff','milestoneBkgColor':'#238636','milestoneBorderColor':'#2EA043','taskTextColor':'#ffffff','taskTextDarkColor':'#ffffff','taskTextLightColor':'#ffffff','taskTextOutsideColor':'#8B949E','gridColor':'#30363D','todayLineColor':'#F85149','titleColor':'#8B949E','sectionBkgColor':'#2F81F714','altSectionBkgColor':'#2F81F70A'}}}%%
gantt
    title A decade of building — 2014 to today
    dateFormat YYYY-MM-DD
    axisFormat %Y
    tickInterval 1year

    section Craft
    Data engineering (pipelines, Spark, Databricks)      :active, de,   2014-01-01, 2026-08-19
    Full-stack engineering (TypeScript, Node, React, AWS) :done,   fs,   2014-01-01, 2021-06-01
    Architecture and platform engineering                :active, arch, 2018-01-01, 2026-08-19

    section AI / ML
    ML and data science                                  :active, ml,   2021-06-01, 2026-08-19
    LLM, RAG and agentic systems                         :active, llm,  2023-06-01, 2026-08-19
    MLOps, evals and guardrails                          :active, ops,  2023-06-01, 2026-08-19

    section Building in public
    Answering on Stack Overflow                          :crit, so,   2015-01-01, 2026-08-19
    Open source on GitHub                                :crit, gh,   2016-01-01, 2026-08-19
    Writing on Medium                                    :crit, med,  2019-01-01, 2026-08-19

    section Milestones
    AI Engineer Lead at Syngenta                         :active,    syn, 2024-05-01, 2026-08-19
    FrameSleuth launch                                   :milestone, fsl, 2025-09-01, 0d
```

---

## Where I Spend My Time

```mermaid
%%{init: {'theme':'base','themeVariables':{'pie1':'#2F81F7','pie2':'#238636','pie3':'#8B949E','pie4':'#D97706','pieOpacity':'1','pieStrokeColor':'#ffffff','pieStrokeWidth':'2px','pieOuterStrokeColor':'#8B949E','pieTitleTextSize':'18px','pieTitleTextColor':'#7A7A7A','pieSectionTextSize':'13px','pieSectionTextColor':'#1F2328','pieLegendTextColor':'#7A7A7A'}}}%%
pie showData
    title Focus areas, right now
    "AI agents, LLM and MCP systems" : 40
    "Data and AI on Databricks" : 25
    "Full-stack product engineering" : 20
    "Technical writing" : 15
```

---

## How I Navigate the Work

Not every problem lives in the same place. I map what I build to the [Cynefin](https://en.wikipedia.org/wiki/Cynefin_framework) domains — because the right approach for a known CRUD API is the wrong approach for a non-deterministic agent.

<p align="center">
  <img src="./assets/cynefin.svg" width="820" alt="A Cynefin map of my current work — Complex (multi-agent orchestration, LLM evals, RAG, FrameSleuth), Complicated (system architecture, Databricks platforms, pipelines), Chaotic (non-deterministic failures, model drift, incidents), Clear (boilerplates, CRUD patterns, CI/release), and Disorder in the center." />
</p>

---

## Featured Projects

**AI, Agents & Products**

| Project | What it is |
| --- | --- |
| **[framesleuth-agent](https://github.com/thestackhub1/framesleuth-agent)** | The open-source MCP server behind FrameSleuth — local video → structured Context Bundle. Python, Docker, pinned lockfile, CI. |
| **[ask-santosh](https://github.com/santoshshinde2012/ask-santosh)** | RAG over my own writing. Retrieval quality (recall@k · MRR) is gated on every push without an API key; DeepEval scores answers when a judge key is set. |
| **[multi-agent-sales-ops-tpch-databricks](https://github.com/santoshshinde2012/multi-agent-sales-ops-tpch-databricks)** | Beyond Genie code — orchestrating production multi-agent systems on Databricks. [Write-up →](https://medium.com/data-science-collective/beyond-genie-code-orchestrating-production-multi-agent-systems-on-databricks-86ac51e9c55b) |
| **[ai-consumption-plane](https://github.com/santoshshinde2012/ai-consumption-plane)** | A hands-on build of the AI Consumption Plane on Databricks. |
| **[churn-vs-risk-poc](https://github.com/santoshshinde2012/churn-vs-risk-poc)** | Why a churn model is not a risk model — and what that costs you. [Write-up →](https://medium.com/ai-that-ships/why-your-churn-model-is-not-a-risk-model-and-why-it-matters-963e1f9bd2e9) |
| **[crop-disease-prediction](https://github.com/santoshshinde2012/crop-disease-prediction)** | End-to-end applied ML: **97.83% across 15 disease classes** in a **9.3 MB** model at **~9 ms**, exported to TFLite and shipped four ways — Streamlit, a FastAPI service, a WhatsApp bot, and a React Native app doing **offline on-device inference**. With a [model card](https://github.com/santoshshinde2012/crop-disease-prediction/blob/main/MODEL_CARD.md) that states where it stops working. |

**Data Engineering & Platform**

| Project | What it is |
| --- | --- |
| **[medallion-architecture-databrics](https://github.com/santoshshinde2012/medallion-architecture-databrics)** | Medallion Architecture — principles and a practical Databricks exploration. [Read →](https://blog.santoshshinde.com/medallion-architecture-principles-and-practical-exploration-425834ae3bc7) |
| **[dataset-atlas](https://github.com/santoshshinde2012/dataset-atlas)** | A map-first way to discover and download datasets — Region → Domain → Get. [Live demo →](https://santoshshinde2012.github.io/dataset-atlas/) |
| **[node-boilerplate](https://github.com/santoshshinde2012/node-boilerplate)** <img src="https://img.shields.io/github/stars/santoshshinde2012/node-boilerplate?style=flat-square&color=D97706&label=%20&logo=github&logoColor=white" alt="stars" /> | Production-ready Node.js + TypeScript skeleton for microservices — ESLint, Prettier, Husky, CI wired in. |
| **[genie-reality-check](https://github.com/santoshshinde2012/genie-reality-check)** | Chart data and methodology behind my Databricks Genie evaluation series. |
| **[delta-live-table-databricks-sample-use-case](https://github.com/santoshshinde2012/delta-live-table-databricks-sample-use-case)** | Declarative pipelines with Delta Live Tables — expectations, lineage and incremental loads. |
| **[delta-lake-databricks-sample-use-case](https://github.com/santoshshinde2012/delta-lake-databricks-sample-use-case)** | Delta Lake from first principles — ACID on object storage, time travel, schema evolution. |
| **[kappa-iot-temperature](https://github.com/santoshshinde2012/kappa-iot-temperature)** | Kappa architecture for real-time IoT temperature monitoring — one streaming path, no batch twin. |
| **[next-genie](https://github.com/santoshshinde2012/next-genie)** | A Next.js front end over Databricks Genie. |

---

## Latest Writing

<!-- BLOG-POST-LIST:START -->
- [Why Your Churn Model Is Not a Risk Model &lpar;And Why It Matters&rpar;](https://medium.com/ai-that-ships/why-your-churn-model-is-not-a-risk-model-and-why-it-matters-963e1f9bd2e9)
- [Databricks Genie: Agent Mode vs Chat Mode — Should You Switch Yet?](https://medium.com/ai-that-ships/databricks-genie-agent-mode-vs-chat-mode-should-you-switch-yet-fc9b8bf65032)
- [Feature Store vs. Gold Data Products: Where Should Your ML Features Live?](https://medium.com/ai-that-ships/feature-store-vs-gold-data-products-where-should-your-ml-features-live-4d75011982a5)
- [What Genie Ontology Actually Automates, and What It Leaves to You](https://medium.com/ai-that-ships/what-genie-ontology-actually-automates-and-what-it-leaves-to-you-95f16458fc85)
- [Data Governance on the Ground — and the Challenges AI Agents Bring](https://medium.com/ai-that-ships/data-governance-on-the-ground-and-the-challenges-ai-agents-bring-49a38acc63cc)
- [Every Design Pattern Casts a Shadow in Machine Learning](https://levelup.gitconnected.com/every-design-pattern-casts-a-shadow-in-machine-learning-c16f727fea02)
- [The Four Debts of AI-Assisted Engineering &lpar;and the Four Gates That Pay Them Down&rpar;](https://levelup.gitconnected.com/the-four-debts-of-ai-assisted-engineering-and-the-four-gates-that-pay-them-down-bd7383acb5f2)
- [Genie’s Two Meters: The One Your Budget Sees, and the One It Doesn’t](https://levelup.gitconnected.com/genies-two-meters-the-one-your-budget-sees-and-the-one-it-doesn-t-23ad1d1dabea)
<!-- BLOG-POST-LIST:END -->

I publish most of this through **[AI That Ships](https://medium.com/ai-that-ships)** — my Medium publication on getting AI systems into production, also on [Substack](https://aithatship.substack.com/). More on [Medium →](https://medium.com/@santosh-shinde)

---

## By the Numbers

<p align="center">
  <img src="https://img.shields.io/github/followers/santoshshinde2012?style=for-the-badge&color=2F81F7&logo=github&logoColor=white&label=followers" alt="followers" />
  <!-- STATS:START -->
  <img src="https://img.shields.io/badge/653-stars%20earned-D97706?style=for-the-badge&logo=github&logoColor=white" alt="stars earned" />
  <img src="https://img.shields.io/badge/144-forks-238636?style=for-the-badge&logo=github&logoColor=white" alt="forks" />
  <img src="https://img.shields.io/badge/2014-building%20here%20since-8B949E?style=for-the-badge&logo=github&logoColor=white" alt="since 2014" />
  <!-- STATS:END -->
</p>

<p align="center"><sub><!-- PRIVATE:START -->Most of my work is in private repositories — <b>1,855 of my last 1,983 contributions</b>, about 94%<!-- PRIVATE:END -->.
These are recounted by the weekly workflow, not typed in by hand.</sub></p>

---

<p align="center">
  <b>What I'm up for.</b><br/>
  Production LLM systems that have to survive contact with real users — retrieval that
  holds up, evals that fail loudly, and the cost and failure-mode work underneath.
  Happy to talk shop, review an eval harness, or compare notes on agent tooling.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/shindesantosh"><img src="https://img.shields.io/badge/Start%20a%20conversation-0A66C2?style=for-the-badge&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://aithatship.substack.com/"><img src="https://img.shields.io/badge/Read%20AI%20That%20Ships-FF6719?style=for-the-badge&logo=substack&logoColor=white" alt="Substack" /></a>
</p>
