"""
we can't use .sort for tuples 
we have to use sorted for tuples

"""

students = ['reza', 'ehsan', 'bahram', 'hossein']
#students.sort(reverse= True)
sorted_students = sorted(students)
for name in sorted_students:
    print(name)

print('----------------------------------\n')

students2 = [('reza', 'F', 60),
             ('ehsan', "A", 33), 
             ('bahram', 'D', 20), 
             ('hossein', 'B', 78)]

students2.sort()  #it sorted base on names
for name in students2:
    print(name)

print('----------------------------------\n')

grade = lambda grades: grades[1]
students2.sort(key=grade)
for name in students2:
    print(name)


print('----------------------------------\n')


age = lambda age: age[2]
students2.sort(key=age)
for name in students2:
    print(name)

print('----------------------------------\n\n\n')

# sorting tuples

students3 = (('reza', 'F', 60),
             ('ehsan', "A", 33), 
             ('bahram', 'D', 20), 
             ('hossein', 'B', 78))

age = lambda age: age[2]
sorted_students3 = sorted(students3, key=age)
for name in sorted_students3:
    print(name)
