from typing import List, Dict
import requests

def get_repository_info(repo_name: str):
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        license_name = data.get("license", {}).get("name", "No license available") if data.get("license") else "No license available"

        return {
            "Repository Name": data.get("name", "N/A"),
            "Owner": data.get("owner", {}).get("login", "N/A"),
            "Description": data.get("description", "No description available"),
            "License": license_name,
            "Creation Date": data.get("created_at", "N/A")
        }
    else:
        return f"Error: {response.status_code} - Could not retrieve repository information"

repo_name = "octocat/Hello-World"
repo_info = get_repository_info(repo_name)
print(repo_info)