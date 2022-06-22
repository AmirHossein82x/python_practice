import csv
name = input("enter you name: ")
city = input('enter you city: ')
age = input('enter your age: ')

with open('student.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'city', 'age'])
    writer.writerow({'name': name, 'city': city, 'age': age})