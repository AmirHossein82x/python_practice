def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    left_half, right_half = split(my_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(my_list):
    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]
    return left, right

def merge(left, right):
    l = []
    i = 0  # index for left list
    j = 0  #index for right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
        
    return l

def verify_sorted(my_list):
    if len(my_list) <= 1:
        return True
    return my_list[0] < my_list[1] and verify_sorted(my_list[1:])



numbers = [2, 1, 4, 10, 9, 45, 22, 13, 56]
print(verify_sorted(numbers))
a = merge_sort(numbers)
print(verify_sorted(a))
