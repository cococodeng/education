https://ru.stackoverflow.com/questions/770949/%D0%A0%D1%83%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F-git-%D0%B2-%D0%BA%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D0%B8

по умолчанию программа _git_ при выводе путей (команды типа `state`, `ls-files`, `diff` и т.п.) символы с кодом больше `0x80` заменяет их восьмиричными кодами (например, `\320\272` для символа «к»).

начиная с [версии 1.5.3](https://github.com/git/git/blob/35f6318d44379452d8d33e880d8df0267b4a0cd0/Documentation/RelNotes/1.5.3.txt) это поведение можно изменить с помощью [конфигурационного параметра](https://www.kernel.org/pub/software/scm/git/docs/git-config.html) `core.quotepath` (принимает значения `true/false` или `on/off`).

для отключения такого преобразования только в текущем хранилище выполните:

```bash
git config core.quotepath false
```

для глобального отключения добавьте опцию `--global`:

```bash
git config --global core.quotepath false
```