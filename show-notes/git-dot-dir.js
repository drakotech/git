/* Examining the Dot Git Directory


Branches are where you will have your branches defined. More
info on that later.

Hooks is where you will have rules defined that will help you
determine what and when to push files if your workplace has a 
very strict push policy.

Info and Exclude will show what we have and what will be
excluded from the version control system. We can add to that
list for security purposes.

Logs is where all the logs of every push that has occurred in 
the application. If you type in 

  git log

this shows all the commit messgaes that we've made so far to
version control. Found under HEAD is the file.
Also under refs is the remotes to show the remote master.
These are some advanced topics so fuzzy right now.

Objects are the objects in memory. Not really a directory you
will ever need to change.

Refs is similar to with logs but actual references that holds
your commit ids for your remotes and tags.

COMMIT EDITMSG  is where your commit messages are stored in
case you ever need to make an update.

Config stores your settings that you set up when you created
the repository link.

Description contains the description to your repo.

HEAD is the reference to where we are currently at.

Index is where it gives our details on what branch we are on
if we are up to date and if there is something to commit.

We have access to all of these elements through the command line
with git log and latest version location etc.

You don't usually have to go into this directory that is the
reason why its hidden.
*/