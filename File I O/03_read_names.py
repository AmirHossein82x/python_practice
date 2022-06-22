names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip("\n"))
for name in sorted(names):
    print(f"My name is {name}")