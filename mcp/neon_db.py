from langchain_core.tools import tool
import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

@tool
def db_query_tool(query: str) -> str:
    """
    Query the PostgreSQL database. 
    Input should be a valid SQL query string.
    Use this for any database related questions.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            if not rows:
                return "No results found."

            result = [" | ".join(columns)]
            result.append("-" * 40)
            for row in rows:
                result.append(" | ".join(str(val) for val in row))

            conn.close()
            return "\n".join(result)

        else:
            conn.commit()
            conn.close()
            return "Query executed successfully."

    except Exception as e:
        return f"Database error: {str(e)}"