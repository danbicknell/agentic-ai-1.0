# from airflow import DAG
# from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import time

def github_api_poller(repo_owner, repo_name, api_endpoint, poll_interval, **kwargs):
    """
    Polls the GitHub API for updates.

    Args:
        repo_owner (str): The owner of the repository (e.g., "octocat").
        repo_name (str): The name of the repository (e.g., "Spoon-Knife").
        api_endpoint (str): The specific API endpoint to poll (e.g., "/issues").
        poll_interval (int): Time in seconds between polls.
        **kwargs: Additional keyword arguments.
    """
    base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    full_url = base_url + api_endpoint
    headers = {"Accept": "application/vnd.github+json"}

    last_updated = None

    while True:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        if data:
            # Assuming the API returns a list of items with an 'updated_at' field
            # Adjust this logic based on your specific API endpoint
            latest_item = max(data, key=lambda x: x.get('updated_at', ''))
            current_updated = latest_item.get('updated_at')

            if current_updated != last_updated:
                print(f"New data found: {current_updated}")
                print(data) # Process the new data here
                last_updated = current_updated
            else:
                print("No new updates.")
        else:
            print("No data returned.")

        time.sleep(poll_interval)



github_api_poller('danbicknell','agentic-ai-1.0','/pulls',60)
