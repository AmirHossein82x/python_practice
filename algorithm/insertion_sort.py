def insertion_sort(my_list):
    for index in range(1, len(my_list)):
        key = my_list[index]
        j = index - 1
        while j >=0 and key < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return my_list

numbers = [2, 4, 1, 0]
print(insertion_sort(numbers))