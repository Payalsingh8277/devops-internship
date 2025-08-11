# Task 4 - Documentation of Commands and Workflow

## Step 1: Create branches
```bash
git checkout main
git pull origin main
git checkout -b feature
git push -u origin feature

git checkout main
git checkout -b dev
git push -u origin dev

## Step 2: Add Task 4 files

- Created folder task4-git-version-control
- Added README.md, .gitignore, TASKS.md

## Step 3: Commit and push changes

git add task4-git-version-control/
git commit -m "Add Task 4 folder with version control documentation"
git push origin feature

## Step 4: Pull Requests on GitHub
- Create PR from feature → dev and merge after review
- Create PR from dev → main and merge after review

## Step 5: Tagging releases
git checkout main
git pull origin main
git tag -a v4.0 -m "Complete Task 4 - Git Version Control"
git push origin v4.0