#git/config 
> Было замечено, что работает неоднозначно, без необходимости не использовать.
```bash
# For Linux OS
git config --global core.autocrlf input
git config --global core.safecrlf true
# For Windows OS
git config --global core.autocrlf true
git config --global core.safecrlf true
```