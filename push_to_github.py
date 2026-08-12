# -*- coding: utf-8 -*-
"""Push pubmed-researcher to GitHub"""
import subprocess
import sys
import json

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, file=sys.stderr, end='')
    return result.returncode

# Check if gh is installed
result = run('where.exe gh')
if result != 0:
    print('\nGitHub CLI not found. Please install it:')
    print('Option 1: Download from https://github.com/cli/cli/releases')
    print('Option 2: Use chocolatey: choco install gh')
    print('Option 3: Use scoop: scoop install gh')
    print('\nOr use the web UI to create the repo at https://github.com/new')
    sys.exit(1)

# Check auth
result = run('gh auth status')
if result != 0:
    print('\nPlease login to GitHub first:')
    print('gh auth login --with-token')
    print('\nThen paste your Personal Access Token.')
    sys.exit(1)

# Create repo
result = run('gh repo create pubmed-researcher --public --description "A Python toolkit for medical literature research built on PubMed E-utilities API" --source=. --remote=origin --push')
print(result)
print('\nDone! Your repo should be live at: https://github.com/YOUR_USERNAME/pubmed-researcher')
