"""
this method is not usefull
"""
import random
def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    while not is_sorted(values):
        random.shuffle(values)
    return values

numbers = [2, 1, 4, 6, 3, 10]
print(bogo_sort(numbers))