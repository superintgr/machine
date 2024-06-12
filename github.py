import os
import git
import subprocess

# 1.  Create a new directory for the project
project_name = "my-python-project"
os.makedirs(project_name, exist_ok=True)

# 2.  Navigate to the project directory
os.chdir(project_name)

# 3. Initialize a Git repository
repo = git.Repo.init(".")

# 4. Create a file
with open("main.py", "w") as f:
    f.write("print('Hello from my project!')")

# 5.  Add the file to the staging area
repo.git.add("main.py")

# 6. Commit the changes
repo.git.commit(m="Initial commit")

# 7. Create a new remote repository on GitHub (using the command line)
#    (Assume you've already logged into GitHub via the command line)
github_repo_name = "my-python-project"
subprocess.run(["gh", "repo", "create", github_repo_name])

# 8. Add the remote repository to your local copy
repo.git.remote.add("origin", f"git@github.com:your-username/{github_repo_name}.git")

# 9. Push your local commits to the remote repository
repo.git.push("origin", "main")

# 10. Clone your repository on another machine (using the command line)
subprocess.run(["git", "clone", f"git@github.com:your-username/{github_repo_name}.git"])

print("Project setup complete!")
