from mcp.brave_search import brave_search_tool
from mcp.github_mcp import github_tool
from mcp.neon_db import db_query_tool

def get_tools():
    return [
        brave_search_tool,
        github_tool,
        db_query_tool,
    ]