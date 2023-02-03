Пример конфига для аутентификации с использованием AUTH-KEY.

```
[user]
	name = Name Surname
	email = e@mail.com
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://repo-name:ghp_KEYHERE@github.com/git-user-name/repo-name.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[credential]
	username = Name Surname
```

How to add token auth and push with it:

```
git clone https://github.com/<GIT_USER_NAME>/<GIT_REPO_NAME>.git
git remote set-url origin https://<GIT_USER_NAME>:<AUTH_TOKEN>@github.com/<GIT_USER_NAME>/<GIT_REPO_NAME>.git
git add .
git commit
git push origin master
```