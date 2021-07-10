/* How to Push a Local Git Repository to GitHub


Go to your github prprofile and create a new repository by
clicking on the + icon.

Enter a name for dyour repository and select if you would like
it to be public or private.

Next you will have some options. You can create a new one from
the command line, push an existing repository, or import code
from another repository.

Creating a new repository on the command line is the git init
create readme file commit and push commands

Pushing an existing repository is when you have already 
started the process locally.

Import is when you would like to start from anothers 
repository.

The commands specific to pushing a new repository is

  git
  -accesses the git library
  remote add
  -links the local directory to the repository
  origin
  -This is the default name/best practice for whoever is hosting
  the repository eg github, gitlab, bitbucket etc
  url
  -url of repository to link

To test this out you can type 
  
  git remote -v 
  //origin  https://github.com/drakotech/javascript.git (fetch)
  //origin  https://github.com/drakotech/javascript.git (push)

This returns the named origin GitHub account. One for pushing
the other for fetching updates.

The reason we have two of these is there are some times you want
users to only have fetch access like for a QA developer for
example.

Next is the command: 

  git push -u origin master

This git command pushes to the origin remote master branch and
sets the defaults for any new pushes.

Then will prompt for password, counts how many objexts will be
passed, writes the objects to the url as the master branch and
sets up tracking.

*/