"""
Guide to Viewing a Version Commit for a Git Project


Whenever you're working with reverting you need to be very
careful that you're only changing the select files that you
want to and so after you perform that investigation you've
brought back your changes from that version to the current
project.

To investigate a commit you are considering reverting back to
you will need to find the version of the application that we
wanted to go lookout. 

git checkout 400e3135d32f8b19c2b315f420a5346cdd0f7996 -b investigation
  We checked it out into an investigation branch and then we
  were able to go through there and cherry-pick the files that
  we wanted to bring back and then all you'd have to do from that
  point is:

git checkout 400e3135d32f8b19c2b315f420a5346cdd0f7996 -- my_file.py
  You could do my path to each one of those files.

"""