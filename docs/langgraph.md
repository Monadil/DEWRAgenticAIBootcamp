---
layout: default
title: "Chapter 3: Langgraph"
nav_order: 4
---

# Chapter 3: Pro-Code Agent Development with Langgraph

Welcome to the most powerful chapter of our course! Here we dive into **pro-code agent development** using Langgraph - giving you complete control over sophisticated AI agent architectures.

## 🎯 Learning Objectives

By the end of this chapter, you'll be able to:
- Understand Langgraph's graph-based agent architecture
- Build agents with persistent memory and conversation history
- Integrate external tools and APIs into your agents
- Create structured output agents with type safety
- Implement search and web scraping capabilities
- Build complex multi-agent workflows with state management

## 📹 Video Tutorial

<div class="video-container">
  <div class="video-placeholder">
    📹 <strong>Video Tutorial Coming Soon!</strong><br>
    <em>Deep dive into building production-ready agents with Python and Langgraph</em>
  </div>
</div>

## 🚀 What is Langgraph?

Langgraph is a library for building stateful, multi-actor applications with LLMs. Key features include:
- **Graph-based architecture** for complex agent workflows
- **Persistent state management** across conversations
- **Tool integration** for external system access
- **Multi-agent coordination** with shared state
- **Streaming support** for real-time interactions
- **Built-in persistence** for production deployments

## 🛠 Setup Instructions

Before diving into the exercises, ensure your environment is ready:

```bash
# Navigate to the Langgraph directory
cd "3. Langgraph"

# Install dependencies (if not already done)
uv sync

# Set up your environment variables
export OPENAI_API_KEY="your-openai-api-key"
export GITHUB_TOKEN="your-github-token"  # For GitHub integration
```

## 📚 Progressive Learning Path

### 0. Basic Agent (`0. basic.py`)

**Objective**: Understand the fundamental Langgraph structure

**What you'll learn**:
- Basic agent setup and configuration
- Simple conversation flow
- State management basics

**Try this**:
```python
python "0. basic.py"
```

### 1. Memory Agent (`1. memory.py`)

**Objective**: Add persistent memory to your agent

**What you'll learn**:
- Conversation history management
- State persistence across sessions
- Memory retrieval and context handling

**Test prompts**:
1. `"My name is Nick, who is Nick?"`
2. Continue the conversation to test memory retention

**Key concepts**:
- **Checkpointing**: Save conversation state
- **Memory retrieval**: Access previous context
- **State updates**: Modify conversation history

### 2. Tool Integration (`2. tool.py`)

**Objective**: Connect your agent to external tools

**What you'll learn**:
- Tool definition and registration
- GitHub API integration
- Structured tool responses

**Test prompt**:
```
"Get me the trending Python repos on GitHub"
```

**Tools demonstrated**:
- GitHub repository search
- API response processing
- Error handling for external services

### 3. Structured Outputs (`3. structured.py`)

**Objective**: Generate type-safe, structured responses

**What you'll learn**:
- Pydantic model integration
- Type safety for agent outputs
- Structured data validation

**Test prompt**:
```
"What are the trending Python repos on GitHub?"
```

**Key features**:
- **Type safety**: Ensure output conforms to expected structure
- **Validation**: Automatic data validation
- **Serialization**: Easy conversion to JSON/other formats

### 4. Search Capabilities (`4. search.py`)

**Objective**: Add web search and information retrieval

**What you'll learn**:
- Web search integration
- Information synthesis from multiple sources
- Search result processing and ranking

**Test prompts**:
```
"What are the six states of the investment oversight framework from digital.gov.au?"
"Give me a summary of the AGA from here https://architecture.digital.gov.au/purpose"
```

**Features**:
- **Web scraping**: Extract content from URLs
- **Search integration**: Query search engines
- **Content synthesis**: Combine information from multiple sources

### 5. Endpoint Review (`5. endpointreview.py`)

**Objective**: Analyze and review web endpoints

**What you'll learn**:
- Automated website analysis
- Content extraction and summarization
- Technical assessment capabilities

**Test with**:
```