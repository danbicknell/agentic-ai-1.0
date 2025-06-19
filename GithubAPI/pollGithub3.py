from github import Github
import pickle

username = "danbicknell"
repo_name = "agentic-ai-1.0"
password = "LNLyy3kimRf5r@R"

git = Github(username, password)
user = git.get_user()
repo = user.get_repos() 


for i in repo:
    
    print(f"Found repository: {i.name}")
        
