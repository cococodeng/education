Настроить тулы:
```bash
# На Windows-Portable-Git использую --system, обычно используют --global.
# Ручное редактирование конфига
git config --system --edit
# dtool (Meld)
git config --system difftool.meld.path "c:\Program Files\Meld\Meld.exe"
git config --system diff.tool meld
# mtool (Sublime Merge)
git config --system mergetool.smerge.path "c:\Soft\Sublime Merge\sublime_merge.exe"
git config --system merge.tool smerge
```

Запустить ручное сравнение:
```bash
meld file1 file2
```
Запустить разрешение merge-conflict:
```bash
git mergetool
```