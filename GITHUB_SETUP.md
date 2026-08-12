# GitHub ??????

## Step 1: Create GitHub Account (if you do not have one)
1. Open https://github.com/signup
2. Register with your email
3. Confirm your email

## Step 2: Create GitHub Personal Access Token
1. Go to https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Check permissions: **repo** (full control)
4. Click **Generate token**
5. **Copy the token** (shown only once!)

## Step 3: Set Up GitHub CLI
Open PowerShell and run:
\\ash
pip install gh
gh auth login --with-token
# Paste your token
\
## Step 4: Create Repository and Push
\\ash
cd C:\Users\User\Desktop\pubmed-researcher
gh repo create pubmed-researcher --public --description "A Python toolkit for medical literature research built on PubMed E-utilities API" --source=. --remote=origin --push
\
## Step 5: Enable GitHub Sponsors
1. Go to https://github.com/sponsors/your-username
2. Click "Create a sponsorship"
3. Set your tiers (e.g., /month for supporters)

## Step 6: Promote
- Post on Twitter/X with #AcademicTwitter #PubMed #Python
- Post on Reddit r/medicalschool, r/bioinformatics
- Post on LinkedIn about your tool
