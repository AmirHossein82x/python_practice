import os 
source = "sample2.txt"
destination = "D:\\bi\\sample1.txt"
try:
    if os.path.exists(destination):
        print("This is already exist! ")
    else:
        os.replace(source, destination)
        print(source, "is moved")
except FileNotFoundError:
    print(source, "is not found")