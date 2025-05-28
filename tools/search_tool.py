def register_search_tool(mcp):
    from langchain_community.tools import DuckDuckGoSearchRun

    @mcp.tool()
    def search_tool(query: str) -> str:
        """
        Search the web for relevant information using DuckDuckGo Search.
        """
        try:
            search = DuckDuckGoSearchRun()
            response = search.invoke(query)
            return response
        except Exception as e:
            return f"An error occurred while invoking DuckDuckGo search tool. Logs: {str(e)}"

