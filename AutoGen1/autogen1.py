import os
import autogen
from autogen import ConversableAgent

#import OpenAI API Key
config_list = autogen .config_list_from_json(env_or_file="connections\OAI_CONFIG_LIST")


# creaete conversable agent
agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": config_list},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)


