**Git Commit-Amend and force push**

```bash
git status && \
git show --stat --oneline HEAD && \
echo "Press enter to Commit-Amend, press CTRL+C to abort" && \
read && \
git add . && \
git commit --amend --no-edit && \
git log --oneline && \
git status && \
echo "Press enter to Force Push, press CTRL+C to abort" && \
read && \
git push origin master -f
```