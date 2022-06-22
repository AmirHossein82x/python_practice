with open("names.txt", "r") as file:
    #line = file.readline()   it will return just first line
    lines = file.readlines()  #it will return a list contain of all lines
for line in lines:
    print(f"My name is {line.rstrip()}")
