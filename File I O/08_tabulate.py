import csv
import tabulate
with open('information.csv', 'r') as file:
    reader = csv.reader(file)
    for name, city, age in reader:

        #print(tabulate.tabulate(reader, tablefmt="grid", headers='keys'))
        with open('new_info01.csv', 'a') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=['name', 'age', 'city'])
            writer.writerow({'name':name.rstrip(), 'city':city.rstrip(), 'age':age.rstrip()})
            