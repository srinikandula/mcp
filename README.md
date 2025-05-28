# Multi-Server MCP Project with OpenAI LLM

## Overview

This project demonstrates a multi-server setup using **MCP (Multi-Channel Protocol)** with multiple tool servers and a client that orchestrates them. The servers expose various tools such as web search, weather lookup, random facts, and PostgreSQL database querying. The client uses OpenAI's LLM to interact with these tools via an agent.

---

## Features

- **Multiple MCP servers** each exposing different tools.
- Tools include:
  - Web search (DuckDuckGo)
  - Weather information (Open-Meteo API)
  - Random fun facts
  - PostgreSQL database querying
- Multi-server client that loads tools from all servers.
- Agent powered by OpenAI LLM (`ChatOpenAI`) that uses tools to answer user queries.
- Modular and clean code structure with explicit tool registration.

---

## Repository Structure

.
├── mcp_server.py # Server 1: Search & Weather tools
├── mcp_server_2.py # Server 2: Random Fact & Postgres tools
├── src
│ └── multi.py # Multi-server client using OpenAI LLM
├── tools
│ ├── init.py
│ ├── mcp_instance.py # MCP instance factory
│ ├── search_tool.py
│ ├── weather_tool.py
│ ├── random_fact_tool.py
│ └── postgres_tool.py
└── README.md

---

## Prerequisites

- Python 3.8+
- OpenAI API key set in environment variable `OPENAI_API_KEY`
- PostgreSQL database accessible at the configured host and credentials
- Required Python packages (see below)

---

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**Example `requirements.txt` includes:**

mcp-server
langchain
langchain-openai
langgraph
psycopg2-binary
requests
pydantic

---

## Configuration

- Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

- Update PostgreSQL connection details in `tools/postgres_tool.py` if needed.

---

## Running the Servers

### Server 1: Search & Weather

```bash
python mcp_server.py
```

### Server 2: Random Fact & Postgres

```bash
python mcp_server_2.py
```

Both servers will run and listen on stdio for MCP client connections.

---

## Running the Multi-Server Client

```bash
python src/multi.py
```

- You will be prompted to enter a query.
- The client will load tools from both servers and use OpenAI LLM to answer your query using the tools.

---

## Example Queries

- "Tell me a fun fact."
- "What’s the weather in New York?"
- "Search for the latest news about space exploration."
- "Run this SQL query: SELECT \* FROM my_table;"

---

## Code Highlights

- **Explicit tool registration:** Each tool defines a `register_<tool>_tool(mcp)` function to register itself with the MCP server instance.
- **Separate MCP instances:** Each server creates its own MCP instance for isolation.
- **Multi-server client:** Connects to multiple MCP servers, loads their tools, and combines them for the agent.
- **OpenAI LLM:** Uses `ChatOpenAI` from `langchain_openai` for language understanding and generation.

---

## Troubleshooting

- If tools do not appear in the client, ensure servers are running and tools are properly registered.
- Check for import errors or exceptions in server logs.
- Verify OpenAI API key is set and valid.
- Confirm PostgreSQL database is reachable and credentials are correct.

---

## Future Improvements

- Integrate local LLMs such as DeepSeek for offline inference.
- Add authentication and security to MCP servers.
- Expand toolset with more APIs and custom tools.
- Add UI frontend for better user experience.
