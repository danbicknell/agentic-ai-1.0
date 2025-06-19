## Assistant Agent

import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient

import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4o", seed=42, temperature=0, api_key=os.getenv("open_oi_api_key"))

    assistant = AssistantAgent(
        name="assistant",
        system_message="You are a helpful assistant.",
        model_client=model_client,
    )

    cancellation_token = CancellationToken()
    response = await assistant.on_messages([TextMessage(content="Hello! Can you tell me the phone number for a taxi?", source="user")], cancellation_token)
    print(response)

    await model_client.close()

asyncio.run(main())
