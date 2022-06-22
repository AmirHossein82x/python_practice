names = ["Ali", "Ahmad", "Reza", "Mohammad", "Hossein"]
with open("names.txt", "a") as file:
    for name in names:
        file.write(f"{name}\n")