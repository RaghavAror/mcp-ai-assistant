# AI Assistant using MCP, LangChain, OpenAI, Groq

An intelligent assistant built using **Model Context Protocol (MCP)** to orchestrate autonomous agents via a **multi-component pattern**, integrating OpenAI/Groq models, LangChain, and a React frontend.

---

## Table of Contents
1. [What is MCP?](#what-is-mcp)
2. [Multi-Component Pattern](#multi-component-pattern)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Core Features](#core-features)
6. [Getting Started](#getting-started)
7. [References](#references)

---

## What is MCP?

**Model Context Protocol (MCP)** is a standard introduced by OpenAI to enable LLM-based agents to:

- Interact with **multiple components or tools** (like browsers, shells, file systems).
- Perform **multi-step reasoning and execution**.
- Simulate a complete agent loop that thinks, plans, and acts using `calls` and `observations`.

🔗 [Official Documentation](https://platform.openai.com/docs/assistants/tools/model-completion-protocol)

---

## Multi-Component Pattern

This project uses a multi-component architecture:

1. **LLM Thought** – Reasoning what to do next.
2. **Tool Call** – Executes a command using MCP.
3. **Observation** – Receives result from tool.
4. **Repeat** – Loop continues until final output.

Each agent runs the above cycle.

---

## Tech Stack

| Layer | Tool/Library | Purpose |
|-------|--------------|---------|
| LLM | OpenAI GPT-4o / Groq | Reasoning, decision-making |
| Agent | LangChain + MCPAgent | Manages multi-step planning |
| Protocol | `mcp-use` SDK | Handles tool calls via MCP |
| Backend | FastAPI + Uvicorn | API to serve agent responses |
| Frontend | React + Vite | Chat UI |
| DB | MongoDB + Motor | Store queries/responses |

---

## Project Structure

```bash
ai-assistant-mcp/
├── backend/
│   ├── main.py
│   ├── mcp_config.json
│   ├── .env
│   └── services/
│       ├── agent_service.py
│       └── db_service.py
├── frontend/
│   ├── src/
│   │   └── components/
│   │       └── ChatUI.jsx
└── database/
    ├── schema.sql
    └── seed_data.sql
