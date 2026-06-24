import streamlit as st
import os
from agent.graph import run_agent

os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
os.environ["GITHUB_TOKEN"] = st.secrets["GITHUB_TOKEN"]
os.environ["DATABASE_URL"] = st.secrets["DATABASE_URL"]

st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("Personal AI Assistant")
st.caption("Powered by Groq · LangGraph · MCP Tools")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "tool_logs" not in st.session_state:
    st.session_state.tool_logs = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response, tool_logs = run_agent(
                st.session_state.messages,
            )

        st.markdown(response)

        if tool_logs:
            with st.expander("Tools used"):
                for log in tool_logs:
                    st.markdown(f"- **{log['tool']}**: {log['input']}")

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })