""" 
How to Delete a Local and Remote Branch in Git


Best practice is to delete your branches once you are done with
them to avoid confusion, especially if there is a lot of time
between working on a branch. It can be difficult to sort through
the clutter.


git branch -d branch-to-remove

#warning: deleting branch 'branch-to-remove' that has been 
# merged to
#         'refs/remotes/origin/branch-to-remove', but not yet
# merged to HEAD.
#Deleted branch branch-to-remove (was 817d3a2).

  This deleted the branch from the local repository and
  hasn't been removed from the remote repository yet.


git push origin --delete branch-to-remove

#To https://github.com/drakotech/git.git
# - [deleted]         branch-to-remove

  This will remove the remote branch from github.com

"""
