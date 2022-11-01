#git/bundle #git/clone
You can do a git bundle: it will compress the repo in one file. It is easy to move one file, as opposed to a all repo with all its files.
```bash
git bundle create /tmp/myrepo.bundle --all
```
See "[How can I email someone a git repository?][1]"
Once copied on Linux, you can clone from that one file.
```bash
git clone myrepo.bundle
cd myrepo
```
  [1]: https://stackoverflow.com/a/2545784/6309


