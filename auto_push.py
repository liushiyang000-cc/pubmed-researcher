import requests
import os
import json

# ?????
# 1. ? https://github.com/settings/tokens ?? Personal Access Token (?? repo)
# 2. ????? YOUR_TOKEN ? YOUR_USERNAME
# 3. ??: python auto_push.py

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE"
USERNAME = "YOUR_GITHUB_USERNAME_HERE"
REPO_NAME = "pubmed-researcher"
REPO_DESC = "A Python toolkit for medical literature research built on PubMed E-utilities API"

def create_and_push():
    if GITHUB_TOKEN == "YOUR_GITHUB_TOKEN_HERE":
        print("Error: ?????? GitHub Token ????")
        print()
        print("?? Token ??:")
        print("1. ?? https://github.com/settings/tokens")
        print("2. ? Generate new token (classic)")
        print("3. ??? repo")
        print("4. ? Generate??? Token")
        return
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # ????
    body = {
        "name": REPO_NAME,
        "description": REPO_DESC,
        "public": True
    }
    resp = requests.post("https://api.github.com/user/repos", headers=headers, json=body)
    if resp.status_code == 201:
        print(f"??????: https://github.com/{USERNAME}/{REPO_NAME}")
    elif resp.status_code == 422:
        print(f"?????: https://github.com/{USERNAME}/{REPO_NAME}")
    else:
        print(f"????: {resp.status_code} {resp.text}")
        return
    
    # ????
    import subprocess
    repo_url = f"https://{USERNAME}:{GITHUB_TOKEN}@github.com/{USERNAME}/{REPO_NAME}.git"
    subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=os.path.dirname(__file__), check=False)
    subprocess.run(["git", "branch", "-M", "main"], cwd=os.path.dirname(__file__), check=False)
    result = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=os.path.dirname(__file__), capture_output=True, text=True)
    if result.returncode == 0:
        print("????!")
    else:
        print(f"????: {result.stderr}")

if __name__ == "__main__":
    create_and_push()
