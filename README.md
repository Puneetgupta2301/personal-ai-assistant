# Personal AI Assistant — MCP + LangGraph + Groq

An agentic AI assistant that autonomously selects and uses tools to answer questions, search the web, interact with GitHub, and query a database — all in a clean chat interface.

**Live Demo:** [your-app.streamlit.app](https://your-app.streamlit.app)

---

## Architecture

User → Streamlit UI → LangGraph Agent → Groq LLM (Llama 3.3 70B)
                                              ↓
                          ┌───────────────────────────────────┐
                          │           MCP Tool Layer           │
                          ├──────────┬──────────┬─────────────┤
                          │   Web    │  GitHub  │  Neon       │
                          │  Search  │   MCP    │  PostgreSQL │
                          └──────────┴──────────┴─────────────┘

---

## Features

- **Web Search** — searches the web in real time using DuckDuckGo
- **GitHub Integration** — list repos, list issues, create issues, search repositories
- **Database Queries** — query PostgreSQL database using natural language
- **Smart Tool Selection** — agent decides which tool to use based on your question
- **Conversation Memory** — remembers full chat history within a session

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Agent Framework | LangGraph |
| LLM | Groq (Llama 3.3 70B) — free |
| Web Search | DuckDuckGo Search — free |
|


---

## Local Setup

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/personal-ai-assistant
cd personal-ai-assistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**
```bash
cp .env.example .env
```

Fill in your keys in `.env`:
```env
GROQ_API_KEY=your_groq_key
GITHUB_TOKEN=your_github_token
DATABASE_URL=your_neon_connection_string
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## Environment Variables

| Variable | Where to get it | Cost |
|---|---|---|
| GROQ_API_KEY | console.groq.com | Free |
| GITHUB_TOKEN | github.com/settings/tokens | Free |
| DATABASE_URL | neon.tech | Free |

---

## Docker Setup

```bash
docker compose up --build
```

App runs at `http://localhost:8501`

---

## Example Queries

| Query | Tool used |
|---|---|
| "What is the latest news in AI?" | Web Search |
| "List all my GitHub repositories" | GitHub MCP |
| "How many users are in the database?" | Neon PostgreSQL |
| "What is LangGraph?" | Direct (no tool) |
| "Search GitHub for RAG examples" | GitHub MCP |

---

## What I Learned

- How LangGraph manages agent state and tool call loops
- How MCP architecture connects AI agents to external tools
- How to deploy agentic AI apps with environment-based secrets

---

## Author

**Puneet Kumar Gupta**  
[LinkedIn](https://linkedin.com/in/pun) · [GitHub](https://github.com/puneetgupta2301)