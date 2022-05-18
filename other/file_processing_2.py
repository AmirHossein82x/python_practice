with open("sample2.txt", "w") as file:
    file.write("hello please enter your password to enter to the program\n")
    file.write("how are you doing today")
    #file.writelines("hello") به آخر فایل نوشته را اضافه می کند
    

    
with open("sample2.txt", "r") as file:
    a = file.read()
    print(a)
#copying file
import shutil
shutil.copyfile("sample2.txt", "helllo.txt")


for i in range(2):
    for j in range(3):
        print("leoolo")