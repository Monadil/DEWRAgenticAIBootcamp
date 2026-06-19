# Visual Agent Development with Langflow
Lab 2 of the DEWR Agentic AI Bootcamp. Build an agent that compares Australian and UK skills priorities live from official government sources, then have a second LLM judge the quality of the comparison (the LLM-as-judge pattern).

## Setup
0. Sign Up: https://astra.datastax.com/signup?type=langflow
1. Go here: https://astra.datastax.com/langflow

## Flow Architecture
```
Chat Input
    │
    ▼
Agent (watsonx.ai / Mistral-Large)
    ├── Firecrawl AU ──► scrapes JSA skills shortage page
    └── Firecrawl UK ──► scrapes UK priority skills page
    │
    ▼ Agent's comparison response
Evaluation Prompt
    │
    ▼
Second LLM (watsonx.ai / Mistral-Large)
    │
    ▼
Chat Output
```

## URLs
| Firecrawl | Country | URL |
|---|---|---|
| Firecrawl 1 | 🇦🇺 Australia | https://www.jobsandskills.gov.au/publications/towards-national-jobs-and-skills-roadmap-summary/current-skills-shortages |
| Firecrawl 2 | 🇬🇧 UK | https://www.gov.uk/government/publications/assessment-of-priority-skills-to-2030/assessment-of-priority-skills-to-2030 |

## Agent Instructions
```
You have a Firecrawl tool. When asked to compare Australian and UK
skills data, always scrape both of these pages:

Australia: https://www.jobsandskills.gov.au/publications/towards-national-jobs-and-skills-roadmap-summary/current-skills-shortages

UK: https://www.gov.uk/government/publications/assessment-of-priority-skills-to-2030/assessment-of-priority-skills-to-2030

Scrape both before answering. Always reference which country
each finding comes from.
```

## Evaluation Prompt (Prompt Template node)
```
Rate this comparison 1–10 on how clearly it explains the
difference between AU and UK.

Give the score, one thing done well, and one thing that
would make it a 10.

{chat_input}
```
> Note: `{chat_input}` receives the **Agent's response**, not the user's original question. The judge never sees the question — it only rates the answer.

## Demo Queries
1. **Shared priorities:** `Which occupations or sectors appear as high priority in BOTH countries?` (expect ~7-8/10)
2. **Care and Digital deep dive:** `Both Australia and the UK are projecting major growth in Care and Digital roles. Compare how each country is describing the challenge and what their skills system needs to deliver.` (expect ~8-9/10)

The score should improve between the two queries — better-framed questions produce better agent outputs.

# Who, When, Why?
👨🏾‍💻 Author: IBM Client Engineering <br />
📅 Version: 2.x<br />
📜 License: This project is licensed under the MIT License </br>
