# tools/postgres_tool.py

def register_postgres_tool(mcp):
    import psycopg2
    from typing import Annotated
    from pydantic import BaseModel

    class PostgresQuery(BaseModel):
        query: Annotated[str, "The SQL query to run on the PostgreSQL database."]

    @mcp.tool()
    def postgres_tool(input: PostgresQuery) -> str:
        """
        Executes a SQL query on a PostgreSQL database and returns the results.
        """
        try:
            conn = psycopg2.connect(
                host="13.201.178.49",
                dbname="postgres",
                user="postgres",
                password="PGadmin@123",
                port=5432
            )
            cursor = conn.cursor()
            cursor.execute(input.query)
            results = cursor.fetchall()
            cursor.close()
            conn.close()

            if not results:
                return "No results found."
            return "\n".join([str(row) for row in results])
        except Exception as e:
            return f"Error accessing DB: {e}"
