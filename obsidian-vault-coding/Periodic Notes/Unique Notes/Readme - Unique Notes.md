- В данной папке находятся заметки, которые трудно категоризовать и упорядочить.
- Заметки носят исторический характер и не представляют особой ценности.
- Рекомендуется переносить ценную информацию из Periodic заметок в основные заметки.
- Решено не добавлять теги в пустой шаблон Periodic заметок. В случае необходимости это можно автоматизировать.
- Удалить пустые заметки можно выполнив из папки `* Notes` команду: 
```bash
# Non-Recursive Deletion of Empty Files
# (https://www.baeldung.com/linux/delete-empty-files-dirs#non-recursive-deletion-of-empty-files)

find . -maxdepth 1 -type f -empty -print -delete
```
- Удалить заметки размером менее 13 байт (только с тэгом)
```bash
find . -name "*.md" -type f -size -13 -print -delete
```
