import os
path = "D:\\exersize_python\\sample2.txt"
if os.path.exists(path):
    print("That location exist")
    if os.path.isfile(path):
        print("This is file")
    else:
        print("This is't file")
else:
    print("That location does't exist")
print("---------------------------------------")

new_path = "D:\\exersize_python"
if os.path.isfile(new_path):
    print('This is a file')
elif os.path.isdir(new_path):
    print("This is a diractory(file)")