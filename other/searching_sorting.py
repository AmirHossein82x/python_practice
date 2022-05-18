from heapq import merge


nums = [3, 1, 4, 2, 5]
# linear search
def search(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1
#print(search(9, nums))

#binary search
def binary_search(x, nums, low, high):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == x:
        return mid
    elif nums[mid] > x:
        return binary_search(x, nums, low, high)
    else:
        return binary_search(x, nums, low, high)
#print(binary_search(2, nums, 1, 5))
 
def iterative_binary_search(x, nums):
    low = 0
    high = len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif x < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1 
#print(iterative_binary_search(4, nums))

#sorting 
def selection_sort(nums, begin):
    n = len(nums)
    if begin == n - 1:
        return
    mp = begin
    for i in range(begin + 1, n):
        if nums[i] < nums[mp]:
            mp = i
    nums[begin], nums[mp] = nums[mp], nums[begin]
    selection_sort(nums, begin + 1)
#print(selection_sort(nums, 1))

def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return 
    mid = n // 2
    lower = nums[:mid]
    upper = nums[mid:]
    merge_sort(lower)
    merge_sort(upper)
    merge(lower, upper, nums)
#print(merge_sort(nums))

def merge(lower, upper, nums):
    nums.clear()
    i, j = 0, 0
    while i < len(lower) and j < len(upper):
        if lower[i] <= upper[j]:
            nums.append(lower[i])
            i += 1
        else:
            nums.append(upper[j])
            j += 1
    while i < len(lower):
        nums.append(lower[i])
        i += 1
    while j < len(upper):
        nums.append(upper[j])
        j += 1
#print(merge(1, 10, nums))
