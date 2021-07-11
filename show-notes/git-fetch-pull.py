""" 
Difference Between Git Fetch and Git Pull


git pull

#remote: Enumerating objects: 5, done.
#remote: Counting objects: 100% (5/5), done.
#remote: Compressing objects: 100% (3/3), done.
#remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
#Unpacking objects: 100% (3/3), 705 bytes | 35.00 KiB/s, done.
#From https://github.com/drakotech/git
#   d1d1bc9..a30f4ad  main       -> origin/main
#Updating d1d1bc9..a30f4ad
#Fast-forward
# README.md | 2 ++

  Is a combination of git fetch and git merge. Processes them
  at the same time.


git fetch

#remote: Enumerating objects: 5, done.
#remote: Counting objects: 100% (5/5), done.
#remote: Compressing objects: 100% (3/3), done.
#remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
#Unpacking objects: 100% (3/3), 729 bytes | 38.00 KiB/s, done.
#From https://github.com/drakotech/git
#   a30f4ad..68a5326  main       -> origin/main

  Fetch is used when you don't have clarity on the situation and
  allows you to have a step inbetween the merge process where
  you can review the changes before manually merging the remote
  and local repositories. Generally the favored choice when you
  have a large number of files to merge with upcoming conflicts.
  Fetch will allow you to have much more granular control over
  fixing those conflicts.


git status

#On branch main
#Your branch and 'origin/main' have diverged,
#and have 1 and 1 different commits each, respectively.
#  (use "git pull" to merge the remote branch into yours)
#
#nothing to commit, working tree clean
  
  Here you can see that the branch has diverged from the main
  branch meaning you have the ability to merge from here. The
  updated changes from the remote branch hasn't been added to
  the local one yet.


git merge origin/main

#Merge made by the 'recursive' strategy.
# README.md | 2 ++
# 1 file changed, 2 insertions(+)

  This will merge the remote and local branches, howeber the
  local branch will be ahead by two commits as seen by:


git status

#On branch main
#Your branch is ahead of 'origin/main' by 2 commits.
#  (use "git push" to publish your local commits)
#
#nothing to commit, working tree clean

  Just requires a commit to bring everything up to speed but
  you can see that the remote changes is now live.

  To complete the process you only need to run:


git push

#Enumerating objects: 16, done.
#Counting objects: 100% (13/13), done.
#Delta compression using up to 8 threads
#Compressing objects: 100% (7/7), done.
#Writing objects: 100% (8/8), 789 bytes | 394.00 KiB/s, done.
#Total 8 (delta 4), reused 0 (delta 0), pack-reused 0
#remote: Resolving deltas: 100% (4/4), completed with 3 local
# objects.
#To https://github.com/drakotech/git.git
#   68a5326..aa7f6ea  main -> main

  Now you will find both commits in the remote repository and
  everything is all synced up, all changes merged and up to 
  date.

"""