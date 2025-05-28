from mcp import Tool
import asyncpg
import asyncio

async def pg_tables_tool(connection_string: str):
    async def tool_fn(query: dict) -> str:
        # Connect to PG and list tables
        conn = await asyncpg.connect(connection_string)
        rows = await conn.fetch(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
        )
        await conn.close()
        tables = [row['table_name'] for row in rows]
        return "Tables: " + ", ".join(tables)
    return Tool(name="PostgresTables", func=tool_fn)

async def load_tools(connection_string: str):
    return [await pg_tables_tool(connection_string)]

