#git 
# Git Rebase Edit
#git/rebase

Если хочу отредактировать commit5 в ветке

> commit7
> commit6
> **commit5**
> commit4

Запускаю:
`git reabse -i`

ставлю напротив этого коммита "e", напротив остальных "p"
```bash
p commit7
p commit6
e commit5
p commit4
```

Редактирую исходники, добавляю изменения в индекс коммита
Делаю коммит
`git commit --amend`
затем
`git rebase -i --continue`

```bash
git submodule init --update --recursive
git submodule update
git submodule update --init --recursive
git rebase --help
git lg
git rebase -i
git lg
git status
git commit --amend
git rebase --continue 
git lg
```

# Git Rebase Squash 
#git/rebase-squash
**Последовательность выполнения Rebase для слияния коммитов (1, 2, 3, 4 -> В один коммит)**

Если надо поправить более ранний коммит (не последний сделанный) и не добавлять новый (мелкие изменения)
В интерфейсе (-i) ребейса выставить возле коммита который нужно слиять со старым i(который хочу немного изменить) ключ s (squash)
(Выставить ключ s возле НОВОГО коммита, и тех на которыее его нужно поменять)

> p commit 1
> s commit 2
> s commit 3
> s commit 4 (тут слияет 4-3-2-1 в коммит4)

```bash
git log --oneline remotes/origin/master..HEAD
git rebase -i
git status
git add -a
git coommit --help
git add -u
git status
git commit
git rebase -i
git show
git show -2
git log -2
git log --oneline remotes/origin/master..HEAD
git push origin 489cd5b:refs/for/master%wip
```

# Картинки Git Rebase Squash

![[Screenshot from 2022-06-02 12-53-30.png]]

![[Screenshot from 2022-06-02 12-55-24.png]]

![[Screenshot from 2022-06-02 12-55-46.png]]

# Заметки с StackOverflow

![[Screenshot from 2022-06-02 13-14-31.png]]

![[Screenshot from 2022-06-02 13-14-39.png]]

![[Screenshot from 2022-06-02 13-14-46.png]]

# Git Rebase (Commit Over Commit)

![[Screenshot from 2022-06-02 16-36-46.png]]

![[Screenshot from 2022-06-02 16-45-56.png]]

![[Screenshot from 2022-06-02 16-46-05.png]]

![[Screenshot from 2022-06-02 16-47-19.png]]

![[Screenshot from 2022-06-02 16-47-31.png]]

Выбираем change ID так, чтобы сохранить ID коммита в GERRIT

![[Выбираем change ID так, чтобы сохранить ID коммита в GERRIT.png]]




