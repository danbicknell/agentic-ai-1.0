from autogen import UserProxyAgent, AssistantAgent
import requests

# Step 1: Define the tool function
def fetch_webpage_content(url: str) -> str:
    """Fetch the contents of a webpage given its URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text[:1000]  # Limit output for readability
    except requests.RequestException as e:
        return f"Error fetching webpage: {e}"

# Step 2: Create the AssistantAgent with the tool
web_fetching_agent = AssistantAgent(
    name="WebFetcher",
    llm_config=False,  # Disable LLM; this agent just runs the tool
    description="Fetches and returns HTML content from a URL.",
    code_execution_config={"use_docker": False},  # or True if needed
    tools=[fetch_webpage_content]
)

# Step 3: Create a UserProxyAgent to interact with the assistant
user = UserProxyAgent(
    name="User",
    code_execution_config=False,
    human_input_mode="NEVER"
)

# Step 4: Initiate the conversation
user.initiate_chat(
    web_fetching_agent,
    message="Fetch the contents of https://example.com"
)
