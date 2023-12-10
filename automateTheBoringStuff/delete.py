import sys
print(sys.executable)


import os
import shutil

import send2trash # pip install send2trash

 # os.rmdir("/Users/absinthe/repos/Python_Playground/automateTheBoringStuff/dummy") # remove empty directory
 
 # shutil.rmtree("/Users/absinthe/repos/Python_Playground/automateTheBoringStuff/dummyFolderBackup") # remove directory and all its contents
send2trash.send2trash("automateTheBoringStuff/dummy") # send directory to trash