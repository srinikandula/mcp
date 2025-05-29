from starlette.applications import Starlette
from starlette.routing import Mount
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport

mcp = FastMCP("Utility Tools SSE")

from tools.search_tool import register_search_tool
from tools.weather_tool import register_weather_tool

register_search_tool(mcp)
register_weather_tool(mcp)

sse = SseServerTransport("/sse")

async def sse_handler(scope, receive, send):
    if scope["type"] != "http":
        await send({
            "type": "http.response.start",
            "status": 400,
            "headers": [(b"content-type", b"text/plain")],
        })
        await send({
            "type": "http.response.body",
            "body": b"Invalid scope type. Expected 'http'.",
        })
        return

    async with sse.connect_sse(scope, receive, send) as (read_stream, write_stream):
        await mcp.run_with_streams(read_stream, write_stream)


# Mount it as an ASGI app
app = Starlette(routes=[
    Mount("/sse", app=sse_handler)
])
