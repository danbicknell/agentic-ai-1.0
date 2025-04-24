# pip install -U "autogen-agentchat" "autogen-ext[openai]"
import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv


load_dotenv()  # take environment variables

async def main() -> None:
    agent = AssistantAgent("assistant", OpenAIChatCompletionClient(model="gpt-4o", api_key=os.getenv("open_oi_api_key")))
    print(await agent.run(task="tell me a joke"))

asyncio.run(main())