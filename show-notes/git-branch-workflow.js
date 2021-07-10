/* Basic Git Branching Workflow

git branch
//* master
  
  Shows what branch you are on, on your local machine. The
  asterisk means you are on the master branch.
 

git checkout -b readme-styling
//Switched to a new branch 'readme-styling'
  
  checkout is the command to use when creating a new branch.
  readme-styling can be anything you'd like to name it. The
  -b flag is what creates a new branch and changes into it.


git branch
//  master
//* readme-styling
  
  Now we are on the readme-styling branch.


git checkout master
//Switched to branch 'master'
//Your branch is up to date with 'origin/main'.
  
checkout without the -b flag is used to switch between
  branches. This will switch you back into the master
  branch.


git branch
//  master
//* readme-styling
  
  Displayed here is that we are back in the 'master' branch.
  Note: the changes made on the readme-styling branch have
  not been merged with the master branch yet.


git merge readme-styling
//Updating 9ddbb2f..b2cc7f7
//Fast-forward
// README.md | 5 +++++
// 1 file changed, 5 insertions(+)
// create mode 100644 README.md

  Here we merge the branches and 'Fast-forward' the master
  branch with the updated README.md files new content.

*/