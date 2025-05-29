# mcp_sse_client.py

import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

async def main():
    # Connect to MCP server SSE endpoint
    async with sse_client("http://localhost:8000/sse/") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            print("Loaded tools:", [tool.name for tool in tools])

            llm = ChatOpenAI(model="o3-mini")

            agent = create_react_agent(
                llm,
                tools=tools,
                prompt=(
                    "You are a helpful assistant with access to tools. "
                    "Always use the tools when relevant."
                )
            )

            # Example query
            response = await agent.ainvoke({"messages": "Tell me a fun fact."})
            print("Agent response:", response['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())

