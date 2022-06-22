import csv
students = []
with open('new_info.csv') as file:
    reader = csv.DictReader(file)
    for sotoon in reader:
        #print(sotoon)
        students.append(sotoon)

#print(students)
for student in students:
    print(f"My name is {student['name']}, I live in {student['city']}, I am {student['age']} years old")