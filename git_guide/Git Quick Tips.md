**Отобразить отличия локальной ветки от удалённой**
```
git diff master origin/master
```
**Отобразить отличия локальной ветки от удалённой (несмёрженный коммит с gerrit.review)**
```
git fetch ssh://AlexanderSosnovsky@review.elvees.com:29418/pre-commit-hooks refs/changes/61/161/37 && git diff FETCH_HEAD -R
```
**Переместить ветку main на 3 родителя над веткой HEAD**
```
git branch -f main HEAD~3
```
**Git Show (Oneline), показать изменяемые в текущем коммите файлы**
```
git show --stat --oneline HEAD
```
**Pre Commit**
```
pre-commit run -a --hook-stage manual
```
Иногда помогает сделать прекомит 2 раза
(Сделать прекомит (авто система проверит и поправит) перед тем как сделать комит)
**Commit Amend**
```
git commit --amend
```
(Добавить исправленные после прекомита файлы к текущему комиту)
**Pull Rebase**
Перед отправкой стянуть актуальное состояние удалённого репозитория
```
git pull --rebase
```
**Git Push to My Personal Repo**
```
git push -u origin master
```
```
git push -f origin master
```
**Git Rebase All Commits**
```
git rebase -i --root
```
**Git Push to [[Git Gerrit]]**
> **ОТПРАВЛЯЕТ ВСЮ ЛОКАЛЬНУЮ ВЕТКУ, 
> ВКЛЮЧАЯ ПРЕДЫДУЩИЕ КОММИТЫ ! ! ! (см `git log`)**
> Рекомендуется дропнуть (`git rebase -i` выставить `d`) нежелетельные для пуша коммиты.
Отправляет коммит с хэшем 6fc7d7d (первые 7 символов, можно целый) в Gerrit 
```
git push origin 6fc7d7d:refs/for/master
```
Отправляет коммит, на который сейчас указывает HEAD
```
git push origin HEAD:refs/for/master
```
Отправляет коммит-родитель коммита, на который сейчас указывает HEAD
```
git push origin HEAD^:refs/for/master
```

Отправляет в Gerrit коммит без доступа на ревью (чтобы ревьювер не видел коммит) (%wip (work in progress))
```
git push origin 6fc7d7d:refs/for/master%wip 
```

**Git Log**
Показывает разницу между удалённым репозитрием и моей локальной копией
```
git log --oneline remotes/origin/master..HEAD
```
Выведет краткий лог
```
git log --oneline
```
