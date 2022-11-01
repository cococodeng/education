#git
# Commit
```bash
#Add Changes to Last commit, but don't create new commit
git commit --amend
# Reset commit author, Reset commit date-time
git commit --amend --reset-author --no-edit
```
# Push
**Git Push to GitHub repo** #git/push [[Git Push]]
```bash
# Force Push (Rewrite origin repo)
git push -f origin master
# Upstream Push
git push --set-upstream origin master
git push -u origin master
# Check upstream with
git branch -vv
```
**Git Push to Gerrit repo** #gerrit #git/gerrit 
> Отправляет всю локальную ветку, включая предыдущие коммиты ! ! ! 
> Cм. `git log`
> Рекомендуется дропнуть нежелательные для пуша коммиты:
> `git rebase -i` выставить `drop` напротив нежелательных коммитов.
> Либо сделать `squash` и объединить коммит с предыдущим коммитом в единый.
```bash
# Отправляет коммит с хэшем 6fc7d7d (первые 7 символов, можно целый хэш) в Gerrit 
git push origin 6fc7d7d:refs/for/master
# Отправляет коммит, на который сейчас указывает HEAD
git push origin HEAD:refs/for/master
# Отправляет коммит-родитель коммита, на который сейчас указывает HEAD
git push origin HEAD^:refs/for/master
```
**Gerrit Push WIP / ACTIVE**
```bash
# Git Push %WIP% to Gerrit (Work in Progress)
# Отправляет в Gerrit коммит без доступа на ревью (чтобы ревьюер не видел коммит и изменения пока не потребуется).
git push origin HEAD:refs/for/master%wip
# Git Push %READY% to Gerrit (Active)
# Снимает пометку Work In Progress с коммита в Gerrit  при пуше.
git push origin HEAD:refs/for/master%ready
```

# Pull
**Pull Rebase** #git/pull
```bash
# Выставить upsteam на origin master ветку.
git branch --set-upstream-to=origin/master master
# Перед пушем рекомендуется стянуть актуальное состояние удалённого репозитория и разрешить конфликты.
git pull --rebase
```
# Rebase
 #git/rebase [[Git Rebase]]
```bash
# Git Rebase All Commits
git rebase -i --root
# Git Rebase interactive continue
git rebase --continue
```
# Reflog
![[Git Reflog]]

# Diff
#git/diff #git/gerrit #git/fetch [[Git Diff]] [[diff-local-remote]]

```bash
# Просмотреть различия через определённый difftool (напрмер, "smerge")
git difftool --tool=smerge
# Отобразить отличия HEAD локальной master-ветки от HEAD удалённой ветки master-ветки
git fetch origin master
git diff HEAD FETCH_HEAD
```
> Отобразить отличия локальной ветки от удалённой (несмёрженный коммит с gerrit.review) 
> Где `refs/changes/61/161/37`
> можно взять из `Download` блока выбранного патчсета.
```bash
git fetch ssh://USER_NAME@REPO_WEBSITE:29418/REPO_NAME refs/changes/61/161/37 && git diff FETCH_HEAD -R
# Отобразить отличия от добавленных в INDEX файлов
git diff --cached
# Отобразить отличия локальной ветки от удалённой
git diff master origin/master
# Сравнить файлы в разных ревизиях (в разных коммитах)
git diff COMMIT^ COMMIT
git diff OLD_COMMIT:filename NEW_COMMIT:filename
git diff HEAD^^^:file HEAD^^:file
```
# Branch
#git/branch
```bash
# Переместить ветку main на 3 родителя над веткой HEAD
git branch -f main HEAD~3
# Удалить ветку
git branch -d <branch>
```
# Restore
#git/restore
**Отмена изменений в индексированных файлах**
Восстановить файлы до версии рабочего каталога (отменить все незакоммиченные изменения) 
!!! Необратимо. Может помочь лишь история изменений в IDE `ctrl+z`.
```bash
# Отменить изменения во всех файлах:
git restore .
# Отменить изменения в одном выбранном файле:
git restore filename
```
# Log
#git/log
```bash
# Показывает разницу между удалённым репозитрием и моей локальной копией:
git log --oneline remotes/origin/master..HEAD
# Выведет краткий лог: 
git log --oneline
# Показать историю изменений файлов между коммитами:
git log -p
# Показать историю изменений одного файла:
git log -p -- filename
```
# Show
#git/show
**Отобразить изменения, добавленные в указанном коммите**
```bash
# Показать график-статисткику изменяемых в текущем коммите файлов:
git show --stat --oneline HEAD
# Показать файл в состоянии указанного коммита
git show REVISION_HASH:path/to/file
git show HEAD~4:src/main.c
```
# Clean
#git/clean
**Очистка Untracked Файлов**

```bash
# Удалить untracked файлы (оставшиеся после разрешения merge-конфликта) (Interactive Clean)
# Выбрать опцию (4: ask each), удалять по необходимости.
git clean -i
# Удалить все Untracked Файлы (Force Clean)
git clean -f
# Удалить все Untracked Файлы (Force Clean) #2
git clean -df
```

# Git Config
#git/config
```bash
#Show path to config file, and show config options:
git config --list --show-origin
#Also show 'system/global/local':
git config --list --show-origin --show-scope
```
