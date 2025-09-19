#!/usr/bin/env python3
import asyncio
from mcp_agent.core.fastagent import FastAgent
import sys

# Create the application
fast = FastAgent("Tool Counter")

# Define the agent - specify servers from config
@fast.agent(instruction="You are a tool counting agent", servers=["filesys"])
async def main():
    async with fast.run() as agent:
        # Try different ways to get tools
        tools = []

        # Check various possible attributes
        if hasattr(agent, 'tools'):
            tools = agent.tools
        elif hasattr(agent, '_tools'):
            tools = agent._tools
        elif hasattr(agent, 'get_tools'):
            tools = await agent.get_tools()
        elif hasattr(agent, 'context') and hasattr(agent.context, 'tools'):
            tools = agent.context.tools
        elif hasattr(agent, '_mcp_aggregator'):
            # Try to get tools from the aggregator
            if hasattr(agent._mcp_aggregator, 'get_tools'):
                tools_dict = await agent._mcp_aggregator.get_tools()
                tools = list(tools_dict.values()) if tools_dict else []
            elif hasattr(agent._mcp_aggregator, 'tools'):
                tools = agent._mcp_aggregator.tools

        # Count and print tools
        tool_count = len(tools) if tools else 0
        print(f"\n=== Tool Count: {tool_count} ===")

        if tool_count > 0:
            print("\nAvailable tools:")
            for i, tool in enumerate(tools, 1):
                if isinstance(tool, dict):
                    tool_name = tool.get('name', 'unknown')
                    tool_desc = tool.get('description', '')[:50] + '...' if tool.get('description') else ''
                    print(f"  {i}. {tool_name}: {tool_desc}")
                else:
                    print(f"  {i}. {tool}")
        else:
            print("\nNo tools found via agent attributes!")
            print("\nChecking aggregator directly...")

            # Try to find the aggregator
            for attr in dir(agent):
                if 'aggregator' in attr.lower() or 'mcp' in attr.lower():
                    print(f"  Found attribute: {attr}")
                    obj = getattr(agent, attr)
                    if hasattr(obj, 'get_tools'):
                        print(f"    - Has get_tools method")
                    if hasattr(obj, 'tools'):
                        print(f"    - Has tools attribute")

        # Exit immediately
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())