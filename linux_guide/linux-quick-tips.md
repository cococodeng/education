#linux
**Print last 20 commands** #linux_history
```bash
history | cut -c 8- | tail -20
```
**Find `foo` file from current directory** #linux_find 
`(. means current, / means root)`
````bash
find . -name "foo*"
````
````bash
find / -name "foo*"
````
````bash
find /some/dir/* -name "foo*"
````
**SSH** #linux_ssh
```bash
ssh company_username@company_pc_name
```
**Modules Load / Unload** #linux_module
*Если модуль не работает (но видится в списке module avail):*
```bash
module unload texlive
module load texlive
```
**Symink** #linux_symlink
Сделать и проверить симлинк
Пример:
```bash
ln -s /usr/corpneo/20220608.tar.gz 20220608.tar.gz
```
```bash
ln -s %FULL_PATH_TO_ORIGINAL_FILE% %DESIRED_SYMLINK_NAME%
```
Затем сделать `ls -lah`, убедиться что у созданного симлинка аттрибут `l` (link) и вес до ~200 байт.
**Show Absolute Path of Subdirs** #linux_ls 
```bash
ls -dv1 $PWD/*                                                                                                                                                                                                   
```
**Find All `dev` files everywhere** #linux_find #regexp 
```bash
find / -regex '^.*/dev$' -type f

# Exclude /proc dir
find / -regex '^.*/dev$' -type f -not -path "/proc/*"
```
**Show All Avaliable terminal commands** #linux_compgen
```bash
compgen -acbk
```
```bash
compgen -ac | grep -iF "utilityNAME"
```
**Grep case insensitive fixed string** #linux_grep
```bash
grep -iF "success..." file1
```
**Find text within files in current directory** #linux_grep
```bash
grep -Ril "text_to_find" ./
```
**Find Text Within All Files** #linux_grep
Parameters: r - recursive, n - show line number in output, i - case insensitive
```bash
grep -rni "text_to_find" *
```
**Extract Archive to Directory** #linux_targz
```bash
tar -xf archive.tar -C /target/directory
```
**Show Full Path to Found-by-Name Files** #linux_find
```bash
find "$PWD" -name "*test*"
```
**Cat Multiple Files**
```bash
xargs cat < list_of_filepathes_saparated_by_newlines
```