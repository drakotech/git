/* Overview of Git Stash


git stash
//Saved working directory and index state WIP on stash-demo:
//8a0e14a Testing rebase complete

  When you need to change into the main branch while working on
  another branch you can use the stash command to put your work
  on a 'hold' state so that you don't lose your progress.

  When you want to reaccess your stashed work you can access it
  with:

git stash list
//stash@{0}: WIP on stash-demo: 8a0e14a Testing rebase complete

  This will return a list of your stashed work with the point in
  time the changes were made, WIP = work in progress.


git stash show
//README.md  | 1 +
// my_file.py | 1 +
// 2 files changed, 2 insertions(+)

  This displays the changes made. If we want to add the changes
  to the branch then:

git stash apply
//On branch stash-demo
//Changes not staged for commit:
//  (use "git add <file>..." to update what will be committed)
//  (use "git restore <file>..." to discard changes in working directory)
//        modified:   README.md
//        modified:   my_file.py
//
//no changes added to commit (use "git add" and/or "git commit -a")

  This will apply the changes ready for commit, however the
  stash will still be there. You will need to clear out your 
  stash with:

git stash clear
  Empties out the stash.

*/