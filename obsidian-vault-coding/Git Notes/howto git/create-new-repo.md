1. Create private or public repo on GITHUB.
2. Rename `main` branch to `master`. (OPTIONAL)
3. Within local directory of repo files `git init`
4. Check Remote URL: `git remote -v`
With Auth Token:
`git remote set-url origin https://<GIT_USER_NAME>:<AUTH_TOKEN>@github.com/<GIT_USER_NAME>/<GIT_REPO_NAME>.git`

OR:
`git remote set-url origin https://github.com/USERNAME/REPOSITORY.git`

4. `git add .` or `git add -A`
5. `git commit`
6. `git push origin master -f` or `git push origin master`