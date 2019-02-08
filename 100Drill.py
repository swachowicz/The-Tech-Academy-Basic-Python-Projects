#   Drill - pull text docs from a particular directory, A

#   use listdir()

#   use path.join()

#   use getmtime()

#   my code:

import os.path, time

fPath = 'C:\\A\\'
      


items = os.listdir(fPath)
#date = time.ctime(os.path.getmtime(fPath))

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
        abPath = os.path.join(fPath + names)
        
        print(names, "last modified time : ",time.ctime(os.path.getmtime(abPath)))


