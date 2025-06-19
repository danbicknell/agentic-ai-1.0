import requests
import os

from dotenv import load_dotenv

# Replace with your repository owner and name
owner = "danbicknell"
repo = "agentic-ai-1.0"

# Replace with your GitHub API token
token = os.getenv("github_api_key")


# Construct the API endpoint URL
url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

# Set up authentication headers
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

try:
    # Make the API request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    pull_requests = response.json()

    # Print some basic information about each pull request
    for pr in pull_requests:
        print(f"Pull Request #{pr['number']}: {pr['title']}")
        print(f"  - URL: {pr['html_url']}")
        print(f"  - State: {pr['state']}")
        print(f"  - Author: {pr['user']['login']}")
        print("-" * 20)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except ValueError as e:
    print(f"JSON decoding error: {e}")
