from langchain_core.tools import tool
from ddgs import DDGS

@tool
def brave_search_tool(query: str) -> str:
    """Search the web for current information using DuckDuckGo."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            if not results:
                return "No results found."
            
            formatted = []
            for r in results:
                formatted.append(f"**{r['title']}**\n{r['body']}\n{r['href']}")
            
            return "\n\n".join(formatted)
    except Exception as e:
        return f"Search failed: {str(e)}"