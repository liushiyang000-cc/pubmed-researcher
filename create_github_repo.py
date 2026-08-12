# -*- coding: utf-8 -*-
import requests
import json

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE"
USERNAME = "YOUR_GITHUB_USERNAME_HERE"
REPO = "pubmed-researcher"

def create_repo():
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Content-Type": "application/json"}
    body = {"name": REPO, "description": "A Python toolkit for medical literature research built on PubMed E-utilities API", "public": True}
    resp = requests.post(f"https://api.github.com/user/repos", headers=headers, json=body)
    if resp.status_code == 201:
        print(f"Repo created: https://github.com/{USERNAME}/{REPO}")
    elif resp.status_code == 422:
        print("Repo already exists!")
    else:
        print(f"Error: {resp.status_code} - {resp.text}")

if __name__ == "__main__":
    create_repo()
