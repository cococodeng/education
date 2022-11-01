TLDR: 
Change username in `.git/config`

```
[user]
    name = New User Name
    email = new_user@mail.com
```

`git commit --amend --reset-author`

Remove contributors list: 
Rename branch name to `main` and rename back to `master`, to remove list of contributors.


# method-1 (command line)

To set your account's default identity globally run below commands

git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git config --global user.password "your password"

To set the identity only in current repository , remove --global and run below commands in your Project/Repo root directory

git config user.email "you@example.com"
git config user.name "Your Name"
git config user.password "your password"

Example:

email -> organization email Id
name  -> mostly <employee Id> or <FirstName, LastName> 

**Note: ** you can check these values in your GitHub profile or Bitbucket profile
method-2 (.gitconfig)

create a .gitconfig file in your home folder if it doesn't exist. and paste the following lines in .gitconfig

[user]
    name = FirstName, LastName
    email = FirstName.LastName@company.com
    password = abcdxyz
[http]
    sslVerify = false
    proxy = 
[https]
    sslverify = false
    proxy = https://corp\\<uname>:<password>@<proxyhost>:<proxy-port>
[push]
    default = simple
[credential]
    helper = cache --timeout=360000000
[core]
    autocrlf = false

Note: you can remove the proxy lines from the above , if you are not behind the proxy

Home directory to create .gitconfig file:

windows : c/users/< username or empID >

Mac or Linux : run this command to go to home directory cd ~

or simply run the following commands one after the other

git config --global --edit
git commit --amend --reset-author
