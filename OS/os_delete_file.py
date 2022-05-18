import os
import shutil
path = "New folder"
try:
    #os.remove(path) # it will delete file
    #os.rmdir(path)  # it will delete empty folder
    shutil.rmtree(path) # it will delete folder and every thing cantains in folder
except FileNotFoundError:
    print("This file does't exist")
except PermissionError: # We does't have permission to delete folder
    print("you don't have permission to delete this file!")
except OSError: # it does't allow us to remove file when it contains file
    print("This file contains files")
else:
    print("%s is removed" %path)