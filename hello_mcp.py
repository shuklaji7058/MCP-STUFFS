from mcp.server.fastmcp import FastMCP
from random import choice

mcp = FastMCP("Random Name")

@mcp.tool()
def get_random_name(names: list = None) -> str:
    """Gets a random peoples names. The names are stored in a local array
    args:
       names:the user can pass in a list of names to choose from, or it will default to a predefined list.
    """

    #If names is provided and not empty, use it; otherwise, use a default list
    if names and isinstance(names, list):
        return choice(names)
    else:
        #Use a default list of names
        default_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        return choice(default_names)

if __name__ == "__main__":
    mcp.run()
