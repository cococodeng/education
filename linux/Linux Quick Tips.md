**Print last 20 commands**
```sh
history | cut -c 8- | tail -20
```
**Find `foo*` file from current `(. means current, / means root)` directory**
````sh
find . -name "foo*"
````
````sh
find / -name "foo*"
````
````sh
find /some/dir/* -name "foo*"
````
**SSH**
```sh
ssh elvees_username@elvees_pc_name
```
**Modules Load / Unload**
*Если модуль не работает (но видится в списке module avail):*
```sh
module unload texlive
module load texlive
```
**Symink**
Сделать и проверить симлинк
Пример:
```sh
ln -s /usr/corpneo/20220608.tar.gz 20220608.tar.gz
```
```sh
ln -s %FULL_PATH_TO_ORIGINAL_FILE% %DESIRED_SYMLINK_NAME%
```
Затем сделать `ls -lah`, убедиться что у созданного симлинка аттрибут `l` (link) и вес до ~200 байт.
**Show Absolute Path of Subdirs**
```sh
ls -dv1 $PWD/*                                                                                                                                                                                                   
```
**Find All `dev` files everywhere**
```sh
find / -regex '^.*/dev$' -type f
find / -regex '^.*/dev$' -type f -not -path "/proc/*"
```
