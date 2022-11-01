How to add token auth and push with it:

```
git clone https://github.com/<GIT_USER_NAME>/<GIT_REPO_NAME>.git
git remote set-url origin https://<GIT_USER_NAME>:<AUTH_TOKEN>@github.com/<GIT_USER_NAME>/<GIT_REPO_NAME>.git
git add .
git commit
git push origin master
```