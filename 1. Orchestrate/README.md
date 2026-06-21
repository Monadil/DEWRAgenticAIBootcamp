# Building Agents with watsonx Orchestrate
Lab 1 of the DEWR Agentic AI Bootcamp. This lab shows how quickly you can build a workforce intelligence agent in watsonx Orchestrate — no code required. The agent answers questions about Australian skills shortages using official Jobs and Skills Australia (JSA) data.

<!-- VIDEO PLACEHOLDER: lab walkthrough video link/thumbnail to be re-added -->

# Sources 📚
| Source | Access method |
|---|---|
| [2025 OSL Key Findings Report (PDF)](https://www.jobsandskills.gov.au/sites/default/files/2025-10/2025%20OSL%20Key%20Findings%20Report_0.pdf) — included in this folder | Knowledge base |
| [JSA Current Skills Shortages (webpage)](https://www.jobsandskills.gov.au/publications/towards-national-jobs-and-skills-roadmap-summary/current-skills-shortages) | Firecrawl scrape |

> Note: Orchestrate's Firecrawl skill uses `/scrape` only — one page per call, no multi-page crawling.

# A. No Tools
Which major occupation groups have persistent shortages and what percentage of persistent shortages does each represent?

What percentage and number of occupations were in national shortage in 2025?

What percentage of jobseekers would need to change the type of jobs they apply for according to the 2024–25 MI?

# B. Adding in Agentic RAG
Upload `2025 OSL Key Findings Report.pdf` as a knowledge base.

Description:
This knowledge base covers Jobs and Skills Australia's 2025 Occupation Shortage List (OSL) Key Findings Report. It contains the national occupation shortage ratings for 2025, how shortage rates have changed since 2024, the top employing occupations rated as being in shortage, and shortage breakdowns by state and territory.

Document-only queries:
- What are the top employing occupations in national shortage in 2025 and how has the overall shortage rate changed from the previous year?
- Which states and territories show the highest occupation shortage ratings in 2025?

# C. Tool
env FIRECRAWL_API_KEY=to be provided in class npx -y firecrawl-mcp

Add: Firecrawl:firecrawl_scrape

Agent instructions:
```
You help DEWR staff understand Australian skills shortages. You have two sources:

1. A knowledge base containing the 2025 OSL Key Findings Report.
2. A Firecrawl scrape tool. When a question needs detail from the current skills
   shortages webpage, scrape:
   https://www.jobsandskills.gov.au/publications/towards-national-jobs-and-skills-roadmap-summary/current-skills-shortages

Always state which source each finding comes from.
```

Web-only query:
- According to https://www.jobsandskills.gov.au/publications/towards-national-jobs-and-skills-roadmap-summary/current-skills-shortages What are the four types of skills shortages and which occupations fall under each category?

# D. Combined Queries (both sources required)
- Which occupations have been in persistent shortage since 2021, and are they still appearing as shortage occupations in the 2025 OSL?
- For Registered Nurses and Electricians, what type of shortage is driving the problem and what does the 2025 data say about whether it's improving or worsening?
- Given that wage increases are rarely used to address shortages, what does the 2025 OSL say about which occupations are most at risk and what interventions might work for each shortage type?
- Which shortage occupations face the worst regional location barriers, and are those same occupations still rated as in shortage nationally in 2025?

# Part 2: From Copilot to Agentic — The Ministerial Brief Agent
Part 1 above is a copilot (you prompt each step). Part 2 is a true agentic system: one trigger starts three agents that gather data and draft a ministerial brief in the Department's standard format — with a human only at the final sign-off gate.

Guided-assembly lab. Everything is pre-built in `Ministerial Brief Agent/`:
- `healthcare-workforce-openapi.yaml` — OpenAPI spec, imported as the Statistics Agent's data tool (a Python fallback, `healthcare_workforce_tool.py`, is included for no-hosting use)
- `Ministerial Brief Format.docx` — the brief format and rules, uploaded as the Writing Agent's knowledge base
- `Agent Prompts.md` — descriptions and instructions for the Orchestrator, Statistics, and Writing agents

Trigger scenario:
Brief the Minister on the current state of the healthcare workforce shortage ahead of the meeting with the AMA (Australian Medical Association).

The Orchestrator calls the Statistics Agent for data, passes it to the Writing Agent to draft against the format knowledge base, and returns the finished brief for sign-off. See the full walkthrough in the [Chapter 1 lab guide](https://monadil.github.io/DEWRAgenticAIBootcamp/orchestrate.html).

# Great resources:
- <a href='https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=getting-started-watsonx-orchestrate'>Getting Started Tutorial</a> - Official IBM documentation.
- <a href='https://developer.watson-orchestrate.ibm.com/'>Deep Dive into ADK</a> - This is ultra useful, it covers the Agent Development Kit.

# Who, When, Why?
👨🏾‍💻 Author: IBM Client Engineering <br />
📅 Version: 2.x<br />
📜 License: This project is licensed under the MIT License </br>
