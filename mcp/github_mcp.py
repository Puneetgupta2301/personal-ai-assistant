from langchain_core.tools import tool
from github import Github
import os

def get_github_client():
    return Github(os.getenv("GITHUB_TOKEN"))

@tool
def github_tool(action: str, repo_name: str = "", title: str = "", body: str = "", query: str = "") -> str:
    """
    Interact with GitHub. 
    Actions: 'list_repos', 'list_issues', 'create_issue', 'search_repos'
    """
    try:
        g = get_github_client()

        if action == "list_repos":
            user = g.get_user()
            repos = list(user.get_repos())[:10]
            result = [f"- {r.full_name} ({'private' if r.private else 'public'})" for r in repos]
            return "Your repositories:\n" + "\n".join(result)

        elif action == "list_issues":
            if not repo_name:
                return "Please provide repo_name to list issues."
            repo = g.get_repo(repo_name)
            issues = list(repo.get_issues(state="open"))[:10]
            if not issues:
                return f"No open issues in {repo_name}"
            result = [f"#{i.number} - {i.title}" for i in issues]
            return f"Open issues in {repo_name}:\n" + "\n".join(result)

        elif action == "create_issue":
            if not repo_name or not title:
                return "Please provide repo_name and title to create an issue."
            repo = g.get_repo(repo_name)
            issue = repo.create_issue(title=title, body=body)
            return f"Issue created: {issue.html_url}"

        elif action == "search_repos":
            if not query:
                return "Please provide a query to search repos."
            repos = g.search_repositories(query=query)
            result = [f"- {r.full_name} ⭐{r.stargazers_count}" for r in repos[:5]]
            return "Search results:\n" + "\n".join(result)

        else:
            return f"Unknown action: {action}. Use list_repos, list_issues, create_issue, or search_repos."

    except Exception as e:
        return f"GitHub error: {str(e)}"