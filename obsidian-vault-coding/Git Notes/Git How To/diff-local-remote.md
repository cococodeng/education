#git/diff

**Show git diff between local `master` and `origin/master`**

```
git fetch origin master
```

```
git diff FETCH_HEAD -R
```

```
git diff --name-only FETCH_HEAD -R
```

```
git diff --name-status FETCH_HEAD -R
```

**Read more**

To compare a local working directory against a remote branch, for example *origin/master*:

 1. ***`git fetch origin master`***
This tells git to fetch the branch named 'master' from the remote named 'origin'.   `git fetch` will **not** affect the files in your working directory; it does not try to merge changes like `git pull` does. `origin` is conventionally your GitHub repo, while `upstream` is typically the original repo, which your repo may be forked from. E.g. say `https://github.com/someorg/someproject` is the `upstream`, while `https://github.com/yourusername/someproject` is your fork of the upstream (your `origin`). So if you make changes to your fork on GitHub and want to fetch those changes locally, you would use `git fetch origin master`. While if the `upstream` has made changes that you need to sync locally before making more changes, you would use `git fetch upstream master`.
 2. ***`git diff --summary FETCH_HEAD`***
When the remote branch is fetched, it can be referenced locally via FETCH_HEAD.  The command above tells git to diff the working directory files against  FETCHed branch's HEAD and report the results in summary format. Summary format gives an overview of the changes, usually a good way to start. If you want a bit more info, use `--stat` instead of `--summary`. 
 3. ***`git diff FETCH_HEAD -- mydir/myfile.js`***
If you want to see changes to a specific file, for example myfile.js, skip the `--summary` option and reference the file you want (or tree).
