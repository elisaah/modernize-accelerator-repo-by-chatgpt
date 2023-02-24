import os
from github import Github

# Enter your GitHub personal access token here
ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')

# Create a PyGithub object using the access token
g = Github(ACCESS_TOKEN)

# Enter the name you want for your new repository
repo_name = 'modernize-accelerator-repo-by-chatgpt'


# Create the new repository under your GitHub account
user = g.get_user()
repo = user.create_repo(repo_name)

# Initialize the repository with a README file
repo.create_file('README.md', 'Initial commit', '# ' + repo_name)

# Create a develop branch
repo.create_git_ref('refs/heads/develop', repo.get_branch('main').commit.sha)

# Set branch protections to prevent force pushes on main and develop branches
branch_names = ['main', 'develop']
for branch_name in branch_names:
    branch = repo.get_branch(branch_name)
    branch.edit_protection(strict=True, enforce_admins=True, required_approving_review_count=1)

print(f'Repository {repo_name} created and initialized successfully!')
