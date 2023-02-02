import requests
import json
import datetime

repo_url = "https://api.github.com/repos/ironhack-datalabs/datamad1020-rev/commits"

# Get the current date and subtract one week
now = datetime.datetime.now()
one_week_ago = now - datetime.timedelta(days=7)

# Make the API request and get the JSON response
response = requests.get(repo_url)
commits = json.loads(response.text)

# Count the number of commits in the past week
count = 0
for commit in commits:
    commit_date = datetime.datetime.strptime(commit["commit"]["committer"]["date"], "%Y-%m-%dT%H:%M:%SZ")
    if commit_date > one_week_ago:
        count += 1

print("Number of commits in the past week:", count)
