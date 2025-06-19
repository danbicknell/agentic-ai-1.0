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

    # Github Docs on the pull request API:
    # https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022
    

    # Print some basic information about each pull request
    for pr in pull_requests:
        print(f"Pull Request #{pr['number']}: {pr['title']}")
        print(f"  - URL: {pr['html_url']}")
        print(f"  - State: {pr['state']}")
        print(f"  - Author: {pr['user']['login']}")
        print(f"  - Number: {pr['number']}")
        # Use An agent to pull the text from the diff URL
        # Then pass the contents to another agent to summarize the changes
        print(f"      - diff url: {pr['diff_url']}")
        print("-" * 20)

    # Example of extracting files changed in the first pull request
        pr_number = pr['number']
        files_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
        print(f"  - Fetching files changed in PR #{pr_number}...")
        response = requests.get(files_url, headers=headers)
        response.raise_for_status()
        files = response.json()
        print(f"  - Files changed in this PR:")
        for f in files:
            print(f"    - {f['filename']}")
            
            print("-" * 20)
            
            
        # Example of fetching the diff for the first pull request
        # -- That said, this pull a lot of metadata, not the actual diff
        #    and is less than useful.  What is needed is the contents of 
        #    the diff_url, which is not returned in the pull request
        #    metadata.

        headers_diff = {
            "Accept": "application/vnd.github.v3.diff"
        }

        response = requests.get(url, headers=headers_diff)

        if response.status_code == 200:
            diff_data = response.text
            # Process the diff_data (e.g., print it, parse it)
            print(diff_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")

            
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except ValueError as e:
    print(f"JSON decoding error: {e}")
