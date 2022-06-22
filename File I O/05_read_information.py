students = []
with open('information.csv') as file:
    for line in file:
        name, city, age = line.rstrip().split(",")
        students.append({"name":name, "city":city, "age":age})

print(students)
for student in sorted(students, key=lambda item: item["city"]):
    print(f"My name is {student['name']}, I live in {student['city']}, I am {student['age']} years old")