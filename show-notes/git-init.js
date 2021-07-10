/* How to Create a Local Git Repository

Create a new directory, then change into it and create a file.
Put some basic code into the file and then run: 

  git init

This is the start of the entire git process that is going
to initialize a new repository inside of this directory. 
Make sure you are in the root of the new project.

This will create a .git directory with everything needed for a
git repository.

Check on the status by runnning:
  
  git status

This will return the status of the repository, letting you know
if you have any changes to commit or if there any files that
are untracked.

You can start tracking them by adding them with:

  git add .

The . says you want to add all files in the directory.

If you run git status again you will see that the files are
now being tracked.

To add the tracked files to your repository you will need to
commit it with:

  commit -m "Message describing this commit"
  
This creates a version ready to be pushed to the github
repository.

*/