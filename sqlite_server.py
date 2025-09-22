from mcp.server.fastmcp import FastMCP
import sqlite3

mcp = FastMCP("Sqlite Server")

@mcp.tool()
def get_top_chatters():
    """"Retrieve the top chatters sorted by number of messages."""

    conn = sqlite3.connect("C:\\Users\\shukl\\OneDrive\\Desktop\\MCP COURSE\\db\\community.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, messages FROM chatters ORDER BY messages DESC")
    results = cursor.fetchall()
    conn.close()

    chatters = [{"name": name, "messages": messages} for name, messages in results]
    return chatters

if __name__ == "__main__":
    mcp.run()