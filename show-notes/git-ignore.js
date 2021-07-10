/* How to Hide Files and Directories from Git with gitignore


Git ignore is the file where you can define what you don't want
to be pushed up to the repository where the entire world would
have access to.

Filename is specific to 

  .gitignore

Anything placed in that file is going to be ignnored. Anything
in that file will not be tracked or added to the commit.

If you ever try to use this code and it doesn't work run:

  git rm --r --cached
  
to remove any cached files that you accidentally added and it
isn't removed by the .gitignore file.
*/