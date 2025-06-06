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

🔗 [Official Documentation](https://platform.openai.com/docs/mcp)

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
```
---

## Core Functionalities

1. Agent Querying
    - **Input a prompt in plain English.**
    - **The agent reasons using LLM and invokes tools via MCP.**
    - **Returns final output to the user.**

2. Agent Execution Logic
```bash
# backend/services/agent_service.py
from mcp_use import MCPClient, MCPAgent
from langchain_openai import ChatOpenAI

client = MCPClient.from_config_file("backend/mcp_config.json")
llm = ChatOpenAI(model="gpt-4o")
agent = MCPAgent(llm=llm, client=client, max_steps=30)
result = await agent.run(query)
```

3. MCP Tool Config
```bash
# backend/mcp_config.json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {
        "DISPLAY": ":1"
      }
    }
  }
}
```

4. Backend API Endpoint
```bash
# backend/main.py
@app.post("/query")
async def query_agent(request: Request):
    data = await request.json()
    query = data.get("query")
    result = await run_agent(query)
    return {"response": result}
```
5. Frontend API Call
```bash
// frontend/src/components/ChatUI.jsx
const res = await fetch("http://localhost:8000/query", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ query }),
});
```
---
## Prerequisites

- Python 3.8+
- Node.js
- MongoDB
- OpenAI Authorization
---


## Getting Started

### Configuration

Ensure you have a `.env` file in your backend directory with the necessary environment variables:

```plaintext
OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=your_mongodb_uri
```

### Backend Setup

1. Navigate to the backend directory and install dependencies.
2. Run the FastAPI server.
```bash
cd backend
uvicorn main\:app --reload
```

### Frontend Setup

1. Navigate to the frontend directory and install dependencies.
2. Start the development server.
```bash
cd frontend
npm install
npm run dev
```

### Running MCP Server

To start the MCP server, use the following command:
```bash
npx @playwright/mcp@latest
```
---

##  References
GitHub for mcp-use:'https://github.com/mcptutorial/mcp-use/blob/main/'

---



