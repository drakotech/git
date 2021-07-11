"""
A Step by Step Guide for How to Resolve Git Merge Conflicts

A git merge conflict is when you and another team member had
made changes to the same file and very same line of code and
having to work through how you resolve that.

git merge origin/main

#Auto-merging my_file.py
#CONFLICT (content): Merge conflict in my_file.py

#On branch main
#Your branch and 'origin/main' have diverged,
#and have 1 and 2 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

#You have unmerged paths.
#  (fix conflicts and run "git commit")
#  (use "git merge --abort" to abort the merge)

#Unmerged paths:
#  (use "git add <file>..." to mark resolution)
#        both modified:   README.md
#        both modified:   my_file.py

#no changes added to commit (use "git add" and/or "git commit -a")

  Here was an attempted merge that encountered some conflicts
  with both modified files (both meaning both local and remote 
  of the same file). Now that you have identified where the 
  conflict lies you can open those files and you will see the
  following in the files with conflicts:

<<<<<<< HEAD
> My innocent little change
=======
> My scary merge conflict code
>>>>>>> origin/main

<<<<<<< HEAD
    print('My local change')
=======
    print('Update python function with merge conflict')
>>>>>>> origin/main

The <<<<<< HEAD section is where the local edits were made and
the ====== is what defines the split between the conflicted code.
The >>>>>> origin/main is referring to the remote edits that
are incoming.

To correct the conflict all thats needed to do is to delete
which section of code you will want to remove, including all
the <<<< and head/origin/main ==== text as well then save the
file and you can reattempt the merge.

"""