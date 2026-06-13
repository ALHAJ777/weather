import requests
import json

USERNAME = "ALHAJ777"  # Replace this

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)
repos = response.json()

if not isinstance(repos, list):
    print("GitHub API Error:")
    print(repos)
    exit()

projects = []

for repo in repos:
    projects.append({
        "name": repo["name"],
        "description": repo.get("description"),
        "url": repo["html_url"],
        "stars": repo["stargazers_count"],
        "language": repo.get("language")
    })

with open("projects.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, indent=2)

print("projects.json generated successfully!")