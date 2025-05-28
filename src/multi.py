from contextlib import asynccontextmanager
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import asyncio

llm = ChatOpenAI(model="o3-mini")

server_params_1 = StdioServerParameters(
    command="python",
    args=["mcp_server.py"],
)

server_params_2 = StdioServerParameters(
    command="python",
    args=["mcp_server_2.py"],
)

@asynccontextmanager
async def agent_context():
    async with stdio_client(server_params_1) as (read1, write1), \
               stdio_client(server_params_2) as (read2, write2):
        async with ClientSession(read1, write1) as session1, \
                   ClientSession(read2, write2) as session2:
            await session1.initialize()
            await session2.initialize()

            tools1 = await load_mcp_tools(session1)
            tools2 = await load_mcp_tools(session2)
            print(f"tools1: {[t.name for t in tools1]}")
            print(f"tools2: {[t.name for t in tools2]}")
            tools = tools1 + tools2

            for tool in tools:
                print(f"Loaded MCP tool: {tool.name}")

            agent = create_react_agent(
                llm,
                tools=tools,
                prompt=("""
                    You are a helpful assistant with access to tools.

                    Whenever a user query can be answered by a tool, **always use the tool**, even if you think you know the answer.

                    Only answer directly if no tool is relevant.
                """)
            )
            yield agent

async def invoke_agent(query):
    async with agent_context() as agent:
        agent_response = await agent.ainvoke({"messages": query})
        print("==== Final Answer ====")
        print(agent_response['messages'][-1].content)

async def main():
    user_query = input("Enter your query: ")
    await invoke_agent(query=user_query)

if __name__ == "__main__":
    asyncio.run(main())

