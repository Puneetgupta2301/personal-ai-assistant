from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from typing import TypedDict, Annotated
import operator
import os

from agent.prompts import SYSTEM_PROMPT
from agent.tools import get_tools

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    tool_logs: list

def run_agent(chat_history: list) -> tuple[str, list]:

    tools = get_tools()
    tool_logs = []
    llm = ChatGroq(
        model="llama3-groq-70b-8192-tool-use-preview",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
    ).bind_tools(tools)

    formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]

    for msg in chat_history:
        if msg["role"] == "user":
            formatted_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            formatted_messages.append(AIMessage(content=msg["content"]))

    tool_map = {tool.name: tool for tool in tools}

    while True:
        response = llm.invoke(formatted_messages)
        formatted_messages.append(response)

        if not response.tool_calls:
            break

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_input = tool_call["args"]

            tool_logs.append({
                "tool": tool_name,
                "input": str(tool_input)
            })

            tool_result = tool_map[tool_name].invoke(tool_input)

            from langchain_core.messages import ToolMessage
            formatted_messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"]
                )
            )

    return response.content, tool_logs