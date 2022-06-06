def binary_search(my_list, target):
    first = 0
    last = len(my_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if my_list[midpoint] == target:
            return midpoint
        elif my_list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(numbers, 12))
print(binary_search(numbers, 4))