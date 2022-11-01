#linux
**Print last 20 commands** #linux/history
```bash
history | cut -c 8- | tail -20
```

**Find `foo` file** #linux/find 
> . means current directory
>  / means root directory

```bash
find . -name "foo*"
find / -name "foo*"
find /some/dir/* -name "foo*"
```

**SSH** #linux/ssh
```bash
ssh company_username@company_pc_name
```

**Modules Load / Unload** #linux/module
Если модуль не работает (но видится в списке `module avail`):
На примере modulename=texlive
```bash
module unload texlive
module load texlive
```

**Symink** #linux/symlink
Сделать и проверить симлинк
Пример:
```bash
ln -s /usr/corpneo/20220608.tar.gz 20220608.tar.gz
```
```bash
ln -s %FULL_PATH_TO_ORIGINAL_FILE% %DESIRED_SYMLINK_NAME%
```
Затем сделать `ls -lah`, убедиться что у созданного симлинка аттрибут `l` (link) и вес до ~200 байт.
**Show Absolute Path of Subdirs** #linux/ls 
```bash
ls -dv1 $PWD/*
```
**Find All `dev` files everywhere** #linux/find #regexp 
```bash
find / -regex '^.*/dev$' -type f

# Exclude /proc dir
find / -regex '^.*/dev$' -type f -not -path "/proc/*"
```
**Show All Avaliable terminal commands** #linux/compgen
```bash
compgen -acbk
```
```bash
compgen -ac | grep -iF "utilityNAME"
```
**Grep case insensitive fixed string** #linux/grep
```bash
grep -iF "success..." file1
```
**Find text within files in current directory** #linux/grep
```bash
grep -Ril "text_to_find" ./
```
**Find Text Within All Files** #linux/grep
Parameters: r - recursive, n - show line number in output, i - case insensitive
```bash
grep -rni "text_to_find" *
```
**Extract Archive to Directory** #linux/targz
```bash
tar -xf archive.tar -C /target/directory
```
**Show Full Path to Found-by-Name Files** #linux/find
```bash
find "$PWD" -name "*test*"
```
**Cat Multiple Files**
```bash
xargs cat < list_of_filepathes_saparated_by_newlines
```