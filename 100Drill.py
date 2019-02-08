#   Drill - pull text docs from a particular directory, A

#   use listdir()

#   use path.join()

#   use getmtime()

#   my code:

import os.path, time

fPath = 'C:\\A\\'

abPath = os.path.join(fPath)
print(fPath)


items = os.listdir("C:\\A\\")
date = time.ctime(os.path.getmtime("C:\\A\\"))

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
        print(names, "last modified: %s" % date)


