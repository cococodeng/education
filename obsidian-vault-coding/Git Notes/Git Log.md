This lets Git generate the patches for each log entry:

	git log -p -- filename


See [`git help log`](https://git-scm.com/docs/git-log) for more options — it can actually do a lot of nice things. :)

---

To get just the diff for a specific commit, use

    git show HEAD

or specify any other revision by identifier.

---

To browse the changes visually:

    gitk

For a graphical view, use [`gitk`][gitk]:

    gitk [filename]

To follow the file across file renames:

    gitk --follow [filename]

[gitk]: https://git-scm.com/docs/gitk/