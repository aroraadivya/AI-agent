import os
import requests
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()
github_token = os.getenv("GITHUB_TOKEN")

def fetch_github(owner, repo, endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"  #made it dynamic so can load any type of repo
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed with status code:", response.status_code)
        return[]
    
    print(data)
    return data

owner = "aroraadivya"
repo = "AI-agent"
endpoint = "issues"  # Example endpoint to fetch issues
fetch_github(owner, repo, endpoint)
