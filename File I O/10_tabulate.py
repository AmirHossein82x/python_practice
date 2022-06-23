import csv
import tabulate

with open('new_info.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(tabulate.tabulate(reader, headers='keys', tablefmt='grid'))