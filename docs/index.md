---
title: Home
layout: default
nav_order: 1
description: "A comprehensive course on building AI agents with Watsonx - from no-code to pro-code solutions"
permalink: /
---

# Nick's Mega Ultra Fun Watsonx Agentic Crash Course

Welcome to the ultimate crash course on building AI agents with Watsonx! This comprehensive course will take you from zero to hero in the world of agentic AI, covering three different approaches to building agents.

## 🎯 Course Overview

This course is designed to give you hands-on experience with building AI agents using different levels of technical complexity. Whether you're a business user, a low-code developer, or a seasoned programmer, there's a path for you.

## 🚀 What You'll Learn

By the end of this course, you'll be able to:
- Build no-code agents using Watsonx Orchestrate
- Create visual agent workflows with Langflow
- Develop sophisticated agents with Langgraph and Python
- Implement proper AI governance and evaluation strategies

## 📚 Course Structure

This course is organized into four progressive sections:

<div class="course-sections">
{% for section in site.course.sections %}
  <div class="section-card">
    <h3><a href="{{ section.page }}.html">{{ section.title }}</a></h3>
    <p>{{ section.description }}</p>
    <div class="video-placeholder">
      📹 <em>Video tutorial coming soon!</em>
    </div>
  </div>
{% endfor %}
</div>

## 🛠 Prerequisites

Before you begin, make sure you have:
- A basic understanding of AI concepts
- Access to Watsonx services (instructions provided in each section)
- Python 3.8+ installed for the Langgraph section
- Git for cloning the repository

## 📁 Repository Structure

```
6-08-2025-DTA/
├── 1. Orchestrate/     # No-code agent building
├── 2. Langflow/        # Low-code visual development
├── 3. Langgraph/       # Pro-code Python development
├── 4. Governance/      # AI governance and evaluation
└── docs/              # Course documentation (this site)
```

## 🎬 Getting Started

1. **Clone the repository**: 
   ```bash
   git clone https://github.com/nicknochnack/6-08-2025-DTA.git
   cd 6-08-2025-DTA
   ```

2. **Install dependencies**:
   ```bash
   pip install uv
   uv sync
   ```

3. **Choose your learning path**:
   - 🆕 **New to AI agents?** Start with [Orchestrate](orchestrate.html)
   - 🔧 **Want visual development?** Jump to [Langflow](langflow.html)
   - 💻 **Ready for coding?** Go to [Langgraph](langgraph.html)
   - 🛡️ **Interested in governance?** Check out [Governance](governance.html)

## 📧 Support

If you have questions or need help:
- Check the README files in each section folder
- Review the code examples and documentation
- Reach out during the course sessions

---

## 👨🏾‍💻 About the Instructor

**Nick Renotte** - AI Engineer and Content Creator  
📅 **Version**: 1.x  
📜 **License**: MIT License

<style>
/* Enhanced Course Styling */
.course-sections {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 25px;
  margin: 40px 0;
}

.section-card {
  border: 1px solid #e1e4e8;
  border-radius: 12px;
  padding: 25px;
  background: #ffffff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.section-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.section-card h3 {
  margin-top: 0;
  margin-bottom: 15px;
  color: #333;
  font-size: 1.4em;
  font-weight: 600;
}

.section-card h3 a {
  text-decoration: none;
  color: #2563eb;
  transition: color 0.2s ease;
}

.section-card h3 a:hover {
  color: #1d4ed8;
  text-decoration: none;
}

.section-card p {
  color: #6b7280;
  margin-bottom: 15px;
  line-height: 1.6;
  font-size: 0.95em;
}

.video-placeholder {
  margin-top: 20px;
  padding: 15px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  color: white;
  text-align: center;
  font-weight: 500;
  box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
}

.video-placeholder em {
  font-size: 0.9em;
  opacity: 0.9;
}

/* Improved typography */
h1 {
  color: #1f2937;
  font-weight: 700;
  margin-bottom: 25px;
}

h2 {
  color: #374151;
  font-weight: 600;
  margin-top: 40px;
  margin-bottom: 20px;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 10px;
}

/* Enhanced lists */
ul li {
  margin: 10px 0;
  line-height: 1.6;
}

/* Code blocks */
code {
  background-color: #f3f4f6;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: 0.9em;
  color: #d73a49;
}

pre {
  background-color: #f6f8fa;
  border-radius: 8px;
  padding: 20px;
  overflow-x: auto;
  border: 1px solid #e1e4e8;
  line-height: 1.4;
}

pre code {
  background: none;
  padding: 0;
  color: #24292e;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .course-sections {
    grid-template-columns: 1fr;
    gap: 20px;
    margin: 30px 0;
  }
  
  .section-card {
    padding: 20px;
  }
  
  h1 {
    font-size: 2em;
  }
  
  h2 {
    font-size: 1.5em;
  }
}
</style> 