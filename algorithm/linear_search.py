def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear_search(numbers, 12))
print(linear_search(numbers, 4))