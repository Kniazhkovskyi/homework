import requests
from typing import List, Dict

def get_recent_commits(repo_name: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits_data = response.json()
        
        recent_commits = []
        for commit in commits_data[:5]:
            commit_info = {
                "Commit Message": commit["commit"]["message"],
                "Author": commit["commit"]["author"]["name"],
                "Date": commit["commit"]["author"]["date"],
                "Link": commit["html_url"]
            }
            recent_commits.append(commit_info)
        
        return recent_commits
    else:
        return [{"Error": f"Error: {response.status_code} - Could not retrieve commit information"}]

repo_name = "octocat/Hello-World"
commits = get_recent_commits(repo_name)

for i, commit in enumerate(commits, 1):
    print(f"Commit {i}:")
    for key, value in commit.items():
        print(f"{key}: {value}")
    print()