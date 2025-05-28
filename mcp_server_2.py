from tools.mcp_instance import create_mcp_instance

mcp = create_mcp_instance("Utility Tools - Facts & Postgres")

from tools.random_fact_tool import register_random_fact_tool
from tools.postgres_tool import register_postgres_tool

register_random_fact_tool(mcp)
register_postgres_tool(mcp)


if __name__ == "__main__":
    mcp.run(transport="stdio") 