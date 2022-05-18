try:
    with open("sample2.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("This file is not find")