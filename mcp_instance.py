from mcp.server.fastmcp import FastMCP

# Each server should create its own MCP instance!
# We'll use a factory function to avoid cross-registration.
def create_mcp_instance(name="Utility Tools"):
    return FastMCP(name)

