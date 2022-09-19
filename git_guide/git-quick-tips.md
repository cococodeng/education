#git
# Commit
**Commit Amend**
```bash
git commit --amend
```
# Push
#git-push [[Git Push]]

**Git Push to My Personal Repo to GitHub**
**Force Push**
```bash
git push -f origin master
```
```bash
git push -u origin master
```

**Git Push to Git Gerrit** #gerrit #git-gerrit 
> ОТПРАВЛЯЕТ ВСЮ ЛОКАЛЬНУЮ ВЕТКУ, 
> ВКЛЮЧАЯ ПРЕДЫДУЩИЕ КОММИТЫ ! ! ! 
> Cм. `git log`)
> Рекомендуется дропнуть (`git rebase -i` выставить `d`) нежелетельные для пуша коммиты.

Отправляет коммит с хэшем 6fc7d7d (первые 7 символов, можно целый хэш) в Gerrit 
```bash
git push origin 6fc7d7d:refs/for/master
```
Отправляет коммит, на который сейчас указывает HEAD
```bash
git push origin HEAD:refs/for/master
```
Отправляет коммит-родитель коммита, на который сейчас указывает HEAD
```bash
git push origin HEAD^:refs/for/master
```

**Git Push %WIP%**
Отправляет в Gerrit коммит без доступа на ревью (чтобы ревьювер не видел коммит) (%wip (work in progress))
```bash
git push origin HEAD:refs/for/master%wip
```
**Git Push %READY%** (Active)
Снимает пометку Work In Progress с коммита в Gerrit  при пуше.
```bash
git push origin HEAD:refs/for/master%ready
```

# Pull
#git-pull

**Pull Rebase**
Перед отправкой стянуть актуальное состояние удалённого репозитория
```bash
git pull --rebase
```

# Rebase
#git-rebase [[Git Rebase]]

**Git Rebase All Commits**
```bash
git rebase -i --root
```
**Git Rebase interactive continue**
```bash
git rebase --continue
```

# Diff
#git-diff [[Git Diff]]

**Отобразить отличия от стянутой master-ветки**
```bash
git fetch origin master

git diff HEAD FETCH_HEAD
```

**Отобразить отличия локальной ветки от удалённой (несмёрженный коммит с gerrit.review)** #git-gerrit #git-fetch
>Где `refs/changes/61/161/37` 
>можно взять из **Download** блока выбранного патчсета.
```bash
git fetch ssh://USER_NAME@REPO_WEBSITE:29418/REPO_NAME refs/changes/61/161/37 && git diff FETCH_HEAD -R
```
**Отобразить отличия от добавленных в INDEX файлов**
```bash
git diff --cached
```
**Отобразить отличия локальной ветки от удалённой**
```bash
git diff master origin/master
```


# Branch
#git-branch

**Переместить ветку main на 3 родителя над веткой HEAD**
```bash
git branch -f main HEAD~3
```

# Restore
#git-restore

**Отмена изменений в индексированных файлах**
Восстановить файлы до версии рабочего каталога (отменить все незакоммиченные изменения) 
( **!!! Необратимо**. Может помочь лишь история изменений в IDE `ctrl+z`.)
```bash
git restore .
```

# Log
#git-log

**Git Log**
Показывает разницу между удалённым репозитрием и моей локальной копией
```bash
git log --oneline remotes/origin/master..HEAD
```
Выведет краткий лог
```bash
git log --oneline
```

# Show
#git-show

**Git Show (Oneline), показать изменяемые в текущем коммите файлы**
```bash
git show --stat --oneline HEAD
```

# Clean
#git-clean

**Очистка Untracked Файлов**
Удалить untracked файлы (оставшиеся после разрешения merge-конфликта)
```bash
git clean -i
```
Выбрать опцию (4: ask each), удалять по необходимости.
**Удалить все Untracked Файлы**
```bash
git clean -f
```
