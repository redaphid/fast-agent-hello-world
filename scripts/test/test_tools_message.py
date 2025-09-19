#!/usr/bin/env python3
import asyncio
from mcp_agent.core.fastagent import FastAgent
import sys

# Create the application
fast = FastAgent("Tool Counter")

# Define the agent with passthrough model to see tools
@fast.agent(
    instruction="You are a tool counting agent",
    servers=["filesys"],
    model="passthrough"  # Use passthrough model for direct testing
)
async def main():
    async with fast.run() as agent:
        # Send a special command to list tools
        response = await agent.send("***CALL_TOOL list_allowed_directories")
        print(f"Tool call response: {response}")

        # Exit
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())