#!/usr/bin/env python3
import asyncio
from mcp_agent.core.fastagent import FastAgent
import sys
import json

# Create the application
fast = FastAgent("Tool Checker")

# Define the agent
@fast.agent(
    instruction="List all available tools",
    servers=["filesys"]
)
async def main():
    async with fast.run() as agent:
        # Try to call a tool to confirm they're loaded
        try:
            # Use the passthrough model temporarily to test
            agent.model = "passthrough"

            # Call the list_allowed_directories tool
            response = await agent.send("***CALL_TOOL list_allowed_directories")

            print("\n=== Successfully called tool! ===")
            print(f"Response: {response}")
            print("\n=== Tools are working! ===")

        except Exception as e:
            print(f"\n=== Error calling tool: {e} ===")

        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())