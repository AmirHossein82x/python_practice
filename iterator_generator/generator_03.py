my_string = 'Hello'
def my_reverse(string):
    for idx in range(len(string)-1, -1, -1):
        yield string[idx]

instance = my_reverse(my_string)
for char in instance:
    print(char)
