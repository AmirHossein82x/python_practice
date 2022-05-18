import functools

letters = ['H', 'E', 'L', 'L', 'O']
word = functools.reduce(lambda x, y,: x + y, letters)
print(word)


numbers = [1, 2, 3, 4, 5]
num = functools.reduce(lambda x, y: x * y, numbers)
print(num)