# Git Cheat Sheet


To selectively merge files from one branch into another branch, run

git merge --no-ff --no-commit branchX
where branchX is the branch you want to merge from into the current branch.

The --no-commit option will stage the files that have been merged by Git without actually committing them. This will give you the opportunity to modify the merged files however you want to and then commit them yourself.

Depending on how you want to merge files, there are four cases:

1) You want a true merge.
In this case, you accept the merged files the way Git merged them automatically and then commit them.

2) There are some files you don't want to merge.
For example, you want to retain the version in the current branch and ignore the version in the branch you are merging from.

To select the version in the current branch, run:

git checkout HEAD file1
This will retrieve the version of file1 in the current branch and overwrite the file1 automerged by Git.

3) If you want the version in branchX (and not a true merge).
Run:

git checkout branchX file1
This will retrieve the version of file1 in branchX and overwrite file1 auto-merged by Git.

4) The last case is if you want to select only specific merges in file1.
In this case, you can edit the modified file1 directly, update it to whatever you'd want the version of file1 to become, and then commit.

If Git cannot merge a file automatically, it will report the file as "unmerged" and produce a copy where you will need to resolve the conflicts manually.

To explain further with an example, let's say you want to merge branchX into the current branch:

git merge --no-ff --no-commit branchX
You then run the git status command to view the status of modified files.

For example:

git status

```bash
# On branch master
# Changes to be committed:
#
#       modified:   file1
#       modified:   file2
#       modified:   file3
# Unmerged paths:
#   (use "git add/rm <file>..." as appropriate to mark resolution)
#
#       both modified:      file4
#
```

Where file1, file2, and file3 are the files git have successfully auto-merged.

What this means is that changes in the master and branchX for all those three files have been combined together without any conflicts.

You can inspect how the merge was done by running the git diff --cached;

git diff --cached file1
git diff --cached file2
git diff --cached file3
If you find some merge undesirable then you can
edit the file directly
save
git commit
If you don't want to merge file1 and want to retain the version in the current branch
Run

git checkout HEAD file1
If you don't want to merge file2 and only want the version in branchX
Run

git checkout branchX file2
If you want file3 to be merged automatically, don't do anything.
Git has already merged it at this point.

file4 above is a failed merge by Git. This means there are changes in both branches that occur on the same line. This is where you will need to resolve the conflicts manually. You can discard the merged done by editing the file directly or running the checkout command for the version in the branch you want file4 to become.

Finally, don't forget to git commit.
