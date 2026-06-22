---
layout: default
title: "Chapter 1: Orchestrate"
nav_order: 2
description: "Building a multi-agent system with watsonx Orchestrate"
---

# Chapter 1: Building a Multi-Agent System with watsonx Orchestrate

Welcome to the first chapter of the DEWR Agentic AI Bootcamp! You'll build a **Ministerial Brief Agent** in watsonx Orchestrate — a team of three agents that, from a single request, gather data, draft a ministerial brief in the Department's standard format, and hand it back for sign-off. No code required.

This is a genuinely *agentic* system: you trigger it once, the agents do the work across a tool and a knowledge base, and a human only steps in at the final gate.

<!-- VIDEO PLACEHOLDER: Intro-Orchestrate — re-insert video embed here -->

## Learning Objectives

By the end of this chapter, you'll be able to:
- Build AI agents in watsonx Orchestrate without writing code
- Import an OpenAPI specification as an agent tool
- Ground an agent in a knowledge base document
- Write clear agent instructions and descriptions
- Orchestrate multiple agents so one request runs end to end
- Run and review a complete agentic workflow

## What is watsonx Orchestrate?

watsonx Orchestrate is IBM's no-code platform for building AI-powered agents and automating business processes. It lets you:
- Create conversational AI agents without programming
- Connect agents to tools (APIs) and knowledge bases
- Compose multiple agents into a coordinated system
- Deploy agents that understand natural language and complete tasks

This lab uses three of its core building blocks: a **tool** (so an agent can pull live data), a **knowledge base** (so an agent is grounded in a documented standard), and **multi-agent orchestration** (so one agent can direct others).

## The Use Case: Ministerial Brief Agent

- **Persona:** Policy Analyst
- **Trigger:** the Minister's office requests a brief
- **Scenario:** *"Brief the Minister on the current state of the healthcare workforce shortage ahead of the meeting with the AMA (Australian Medical Association)."*
- **Outcome:** a ministerial brief with cited statistics, produced autonomously in the Department's standard format, ready to route for sign-off.

![Ministerial Brief Agent architecture](assets/images/multiagent-architecture.svg)

| Agent | Role |
|---|---|
| **Orchestrator** | Decomposes the request and sequences the two sub-agents |
| **Statistics Agent** | Calls the healthcare workforce tool and formats the metrics into citation-ready text |
| **Writing Agent** | Drafts the brief in the Department's standard format, grounded in a knowledge base that defines that format |

> All figures in this lab are illustrative mock data, clearly labelled — not official ABS/JSA statistics.

## Setup Instructions

You'll need:
- Access to a watsonx Orchestrate instance (details provided in class)
- The two provided files from `1. Orchestrate/Ministerial Brief Agent/`:
  - `healthcare-workforce-openapi.yaml` — the data tool (imported in Exercise A)
  - `Ministerial Brief Format.docx` — the brief format knowledge base (uploaded in Exercise B)

All three agent prompts below are also in `Agent Prompts.md` for easy copy-paste.

## Course Exercises

Build the two sub-agents first, then the Orchestrator that directs them.

### Exercise A: Statistics Agent

This agent fetches the healthcare workforce data and returns it as cited text. Create a new agent named **Statistics Agent** and import `healthcare-workforce-openapi.yaml` as an OpenAPI tool (it exposes a `getHealthcareWorkforce` operation that returns the workforce figures). Then paste its Description and Instructions.

**Description**

```
Retrieves current healthcare workforce statistics from the workforce data tool and
returns them as citation-ready figures with their source and period. Use it when a brief
needs sourced employment and shortage data.
```

**Instructions**

```
You retrieve healthcare workforce statistics for ministerial briefs. Call the healthcare
workforce tool to get the data, then return the figures as citation-ready text — each with
its source and period, e.g. "312,400 Registered Nurses employed, April 2026 (JSA
Occupation Shortage List 2025)". Return the role figures and the sector summary. Use only
the numbers the tool returns; never invent or estimate figures.
```

**Test it:** ask *"Show me healthcare workforce statistics."* You should get the roles and the sector summary, each figure cited.

### Exercise B: Writing Agent

This agent drafts the brief, grounded in the format knowledge base. Create a new agent named **Writing Agent** and upload `Ministerial Brief Format.docx` as its knowledge base — it defines the required structure and rules (purpose line, key points limit, citations, background length, suggested talking points, and so on). Then paste its Description and Instructions.

**Description**

```
Drafts ministerial briefs in the Department's standard format from a topic and supplied
statistics. Use it to produce a brief.
```

**Instructions**

```
You draft ministerial briefs for DEWR. Follow the structure and rules in the Ministerial
Brief Format document in your knowledge base, and match the clean style of its worked
example — do not include any rule labels or word-count notes in the brief.

Use only the statistics the Statistics Agent provides, and cite each figure as "(JSA
Occupation Shortage List 2025, April 2026)". Do not add figures or sources from your own
knowledge. If a particular metric is not in the data, leave it out and write the brief
from what you have.
```

### Exercise C: Orchestrator Agent

This agent ties it together — it calls the Statistics Agent, then the Writing Agent. Create a new agent named **Ministerial Brief Agent** (the orchestrator) and add the Statistics Agent and Writing Agent as collaborators it can call. Then paste its Description and Instructions.

**Description**

```
Produces ministerial briefs on workforce topics for the Department of Employment and
Workplace Relations. It gathers the relevant statistics, drafts the brief in the
Department's format, and returns it for human sign-off. Use it whenever the Minister's
office requests a brief.
```

**Instructions**

```
You coordinate ministerial briefs for the Department of Employment and Workplace
Relations. When someone requests a brief:
1. Identify the topic and the statistics needed.
2. Call the Statistics Agent to get the relevant workforce data with sources.
3. Pass the topic and the data to the Writing Agent to draft the brief.
4. Return the finished brief for human sign-off.

Work with whatever data the Statistics Agent returns — do not ask for extra figures it
does not provide, and do not refuse a brief because a specific metric is missing. State
the source of each figure, never invent statistics, and give no policy or political
opinions.
```

### Exercise D: Run It End to End

Trigger the Orchestrator with the scenario:

```
Brief the Minister on the current state of the healthcare workforce shortage
ahead of the meeting with the AMA (Australian Medical Association).
```

Watch it work on its own: the Orchestrator calls the Statistics Agent for data, passes it to the Writing Agent to draft against the format knowledge base, and returns a finished brief. You triggered it once; the agents did the rest, and you review the result at the gate.

## Example Output

```
OFFICIAL: Sensitive

BRIEF TO THE MINISTER
Employment and Workplace Relations

SUBJECT: Healthcare workforce shortage — background for AMA meeting

PURPOSE: To inform the Minister of current healthcare workforce conditions
ahead of the meeting with the Australian Medical Association.

KEY POINTS:
• 48% of healthcare occupations are in national shortage
  (JSA Occupation Shortage List 2025)
• Registered Nurses most acute: 312,400 employed April 2026, down 1,200 from March
• Retention gap is the primary driver — workers leaving faster than training
  pipelines can replace
• Regional fill rates (62.9%) lag metro (69.7%)

BACKGROUND: ...

FINANCIAL IMPLICATIONS: No direct financial implications.

SUGGESTED TALKING POINTS:
• The Government recognises healthcare workforce pressures, with 48% of
  occupations in national shortage (JSA Occupation Shortage List 2025)
• Retention — not only training — is central; it is the primary driver
• Regional access is a focus: regional fill rates (62.9%) lag metro (69.7%)

ACTION: For Noting

Contact: [Name] | [Title] | [Phone] | April 2026
```

## Essential Resources

- [Getting Started Tutorial](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=getting-started-watsonx-orchestrate) - Official IBM documentation
- [Agent Development Kit (ADK)](https://developer.watson-orchestrate.ibm.com/) - Deep dive into advanced development features

## Next Steps

You've built a multi-agent system that turns one request into a finished, formatted brief. Next:

**[Chapter 2: Langflow](langflow)** - Visual, low-code agent development

---

## Related Files

```
1. Orchestrate/
├── README.md                                 # Lab reference guide
└── Ministerial Brief Agent/
    ├── Ministerial Brief Format.docx         # Writing Agent knowledge base (format + rules)
    ├── healthcare-workforce-openapi.yaml     # Statistics Agent data tool (OpenAPI)
    ├── healthcare_workforce_tool.py          # No-hosting Python fallback for the tool
    ├── DPMC Brief Standards.md               # Text version of the brief format
    └── Agent Prompts.md                      # The three agent prompts and descriptions
```
