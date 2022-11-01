#git/submodule #git #LaTeX
https://gerrit.companyname.com/admin/repos/mcom03/uspd,general

Делаем так, т.к. этот метод подтягивает обновления сабмодуля из remote-ветки.
```bash
# Обновляет субмодуль до состояния коммита-родителя
git submodule update --init 

# Обновляет субмодуль до состояния глобального репозитория
git submodule update --remote --merge 

# Показывает Update uspd submodule патчноут об обновлении сабмодуля
git submodule summary 
```
 обновляет субмодуль до состояния коммита-родителя
`git submodule update --init`

обновляет субмодуль до состояния глобального репозитория
`git submodule update --remote --merge`

Update uspd submodule
`git submodule summary`

Git Update Submodule
```bash
git submodule update --init --recursive
```