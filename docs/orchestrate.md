---
layout: default
title: "Chapter 1: Orchestrate"
nav_order: 2
description: "Building no-code AI agents with watsonx Orchestrate"
---

# Chapter 1: Building Agents with watsonx Orchestrate

Welcome to the first chapter of the DEWR Agentic AI Bootcamp! This section introduces **no-code agent building** using watsonx Orchestrate. You'll build a workforce intelligence agent that answers questions about Australian skills shortages, grounded in official Jobs and Skills Australia (JSA) data.

<!-- VIDEO PLACEHOLDER: Intro-Orchestrate — re-insert video embed here -->

## Learning Objectives

By the end of this chapter, you'll be able to:
- Understand what watsonx Orchestrate is and how it works
- Build agents without writing any code
- Integrate tools and knowledge bases into your agents
- Create agentic RAG (Retrieval Augmented Generation) solutions grounded in official government data
- Use external tools like Firecrawl for live web scraping
- Combine two sources to answer questions that neither source could answer alone

## What is watsonx Orchestrate?

watsonx Orchestrate is IBM's no-code platform for building AI-powered agents and automating business processes. It allows you to:
- Create conversational AI agents without programming
- Connect to various data sources and APIs
- Build complex workflows using a visual interface
- Deploy agents that can understand natural language and perform tasks

## The Use Case: Workforce Intelligence

Throughout this lab your agent will reason over two official sources:

| Source | What it provides | How the agent accesses it |
|---|---|---|
| **2025 OSL Key Findings Report (PDF)** | Annual occupation shortage ratings, 2024→2025 trends, top employing occupations in shortage, state and territory breakdowns | Knowledge base (agentic RAG) |
| **JSA Current Skills Shortages (webpage)** | Shortage typology (Longer Training Gap / Shorter Training Gap / Suitability Gap / Retention Gap), Top 20 occupations in demand, regional barriers, wage analysis | Firecrawl web scraping |

- PDF: [2025 OSL Key Findings Report](https://www.jobsandskills.gov.au/sites/default/files/2025-10/2025%20OSL%20Key%20Findings%20Report_0.pdf) (also included in the `1. Orchestrate/` folder)
- Webpage: [JSA Current Skills Shortages](https://www.jobsandskills.gov.au/publications/towards-national-jobs-and-skills-roadmap-summary/current-skills-shortages)

> **Note:** Orchestrate's Firecrawl skill uses `/scrape` only — it fetches a single page per call. There is no multi-page crawling, so always point the agent at the exact page you need.

## Setup Instructions

Before we begin, you'll need:
- Access to a watsonx Orchestrate instance (details provided in class)
- A Firecrawl API key for Exercise C (provided in class)

## Course Exercises

### Exercise A: Basic Agent Interactions

<!-- VIDEO PLACEHOLDER: Orchestrate1-Basic — re-insert video embed here -->

Create an agent with no tools or knowledge attached, and start with these warm-up questions:

1. **"What is a skills shortage, and how do governments typically measure one?"**
   - Tests the agent's general understanding of labour market concepts
   - Observe how the agent structures its response

2. **"What is the difference between a labour shortage and a skills gap?"**
   - Tests precision with closely related terminology
   - Notice whether the agent distinguishes the two cleanly

3. **"How could an ageing population change Australia's labour market over the next decade?"**
   - Complex, open-ended reasoning question
   - Shows the agent's ability to provide structured analysis

**Observation point:** these answers come entirely from the model's training data. They're fluent, but there are no citations and no current figures. The next two exercises fix exactly that.

### Exercise B: Adding Agentic RAG

<!-- VIDEO PLACEHOLDER: Orchestrate2-RAG — re-insert video embed here -->
<!-- SCREENSHOT PLACEHOLDER: knowledge base configuration in Orchestrate -->

Now we'll ground the agent in current, official data by uploading the **2025 OSL Key Findings Report** PDF as a knowledge base.

**Knowledge Base Description:**
> This knowledge base covers Jobs and Skills Australia's 2025 Occupation Shortage List (OSL) Key Findings Report. It contains the national occupation shortage ratings for 2025, how shortage rates have changed since 2024, the top employing occupations rated as being in shortage, and shortage breakdowns by state and territory.

**Try these document-only prompts** (only the PDF can answer them):

```
What are the top employing occupations in national shortage in 2025
and how has the overall shortage rate changed from the previous year?
```

```
Which states and territories show the highest occupation shortage
ratings in 2025?
```

**Why these work:** the year-on-year comparison and the top employing occupations list only exist in the PDF — the agent must retrieve from the knowledge base rather than answer from memory.

### Exercise C: External Tool Integration

<!-- VIDEO PLACEHOLDER: Orchestrate3-MCP — re-insert video embed here -->
<!-- SCREENSHOT PLACEHOLDER: Firecrawl tool added to the agent -->

Learn to integrate external tools for live web data:

1. **Set up the Firecrawl tool**:
   ```bash
   env FIRECRAWL_API_KEY=your_api_key_here npx -y firecrawl-mcp
   ```

2. **Add the tool**: `Firecrawl:firecrawl_scrape`

3. **Update the agent's instructions** so it knows when to scrape:
   ```
   You help DEWR staff understand Australian skills shortages. You have
   two sources:

   1. A knowledge base containing the 2025 OSL Key Findings Report.
   2. A Firecrawl scrape tool. When a question needs detail from the
      current skills shortages webpage, scrape:
      https://www.jobsandskills.gov.au/publications/towards-national-jobs-and-skills-roadmap-summary/current-skills-shortages

   Always state which source each finding comes from.
   ```

4. **Test with this web-only prompt** (only the webpage can answer it):
   ```
   What are the four types of skills shortages and which occupations
   fall under each category?
   ```

**Why this works:** the shortage typology (Longer Training Gap / Shorter Training Gap / Suitability Gap / Retention Gap) and the Top 20 occupations in demand table only exist on the webpage — not in the PDF.

### Exercise D: Two-Source Reasoning

This is the payoff. These queries can only be answered by **combining** the knowledge base and the scraped webpage — neither source alone is enough:

```
Which occupations have been in persistent shortage since 2021,
and are they still appearing as shortage occupations in the 2025 OSL?
```

```
For Registered Nurses and Electricians, what type of shortage is
driving the problem and what does the 2025 data say about whether
it's improving or worsening?
```

```
Given that wage increases are rarely used to address shortages, what
does the 2025 OSL say about which occupations are most at risk and
what interventions might work for each shortage type?
```

```
Which shortage occupations face the worst regional location barriers,
and are those same occupations still rated as in shortage nationally
in 2025?
```

**Teaching point:** the most powerful agent demos require two-source reasoning. Watch how the agent scrapes the webpage for shortage types and historical persistence, then cross-references the knowledge base for the latest 2025 ratings.

## Essential Resources

- [Getting Started Tutorial](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=getting-started-watsonx-orchestrate) - Official IBM documentation
- [Agent Development Kit (ADK)](https://developer.watson-orchestrate.ibm.com/) - Deep dive into advanced development features

## Key Concepts

### No-Code Development
- **Visual Interface**: Build agents using drag-and-drop components
- **Natural Language**: Configure agents using plain English descriptions
- **Pre-built Integrations**: Connect to popular business applications without coding

### Agentic RAG
- **Knowledge Integration**: Add custom knowledge bases to your agents
- **Context-Aware Responses**: Agents provide answers based on your specific documents
- **Grounded Answers**: Responses cite current official data rather than training data

### Tool Integration
- **External APIs**: Connect to web services and databases
- **Real-time Data**: Access current information from live sources
- **Two-Source Reasoning**: Combine a knowledge base and a live tool to answer questions neither could alone

## Practice Exercises

1. **Employment Data Digest**:
   - Point Firecrawl at the [ABS Labour Force latest release](https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release)
   - Ask the agent to produce key statistics for program managers

2. **Labour Market Policy Briefer**:
   - Ask the agent for a three-paragraph Ministerial briefing combining the OSL knowledge base and the scraped webpage
   - Check whether each claim is attributed to the right source

3. **Occupation Shortage Explainer for Employers**:
   - Ask for a plain-English explainer an employer could read in two minutes
   - Compare how the agent simplifies the shortage typology

## Next Steps

Once you've mastered no-code agent building with Orchestrate, you're ready to move on to:

**[Chapter 2: Langflow](langflow)** - Learn visual, low-code agent development

---

## Related Files

All the code and resources for this chapter can be found in:
```
1. Orchestrate/
├── README.md                            # Lab reference guide
└── 2025 OSL Key Findings Report.pdf     # Knowledge base document
```
