from tools.mcp_instance import create_mcp_instance

mcp = create_mcp_instance("Utility Tools - Search & Weather")

from tools.search_tool import register_search_tool
from tools.weather_tool import register_weather_tool

register_search_tool(mcp)
register_weather_tool(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")

