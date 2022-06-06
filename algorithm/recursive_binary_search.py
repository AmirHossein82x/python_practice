def recursive_binary_search(my_list, target):
    if len(my_list) == 0:
        return False
    else:
        midpoint = len(my_list) // 2
        if my_list[midpoint] == target:
            return True
        elif my_list[midpoint] < target:
            return recursive_binary_search(my_list[midpoint+1:], target)
        else:
            return recursive_binary_search(my_list[:midpoint], target)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recursive_binary_search(numbers, 12))
print(recursive_binary_search(numbers, 5))