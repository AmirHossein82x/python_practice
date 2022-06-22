import csv
students = []
with open('information.csv') as file:
    reader = csv.reader(file)
    for name, city, age in reader:
        student ={"name": name, 'city': city, 'age': age}
        students.append(student)

for student in students:
    print(f"My name is {student['name']}, I live in {student['city']}, I am {student['age']} years old")