import csv
import tabulate

with open('information.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(tabulate.tabulate(reader, headers='keys', tablefmt='grid'))