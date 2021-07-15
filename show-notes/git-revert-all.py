"""
How to Revert an Entire Project Back to a Previous Version in
Git


Be careful when attempting to revert an entire project to a
previous version, this isn't something that is done often
because you are essentially rewriting history. You are removing
a chunk of time, be it 2 commits or 20 commits. When you view
the commit history, you are going to see that all those changes
were completely removed.

This can be even more dangerous when you are working with a team
because you can cause a lot of conflicts while attempting this.

The safest method would be to find the select files you would
like to revert instead of the entire project and risk changing
the entire history of the project.

Essentially what we are doing is resetting the HEAD pointer.

When you select a commit that you want to revert to all changes
after it will be removed completely. There are some messy
topics to attempt to recover these commits.

After you perform an investigation by creating a new branch
of the commit in question you can revert the local repository
by running:

git reset --hard 596b0073b3e4975f62b5531577f871ef4cc38abf
#HEAD is now at 596b007 Updateg gitignore file to include
#node_modules directory

Force this to the remote repository by running:

git push -f origin main



"""