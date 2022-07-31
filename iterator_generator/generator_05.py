def my_gen(end):
    start = 1
    while start <= end:
        yield start ** 3
        start += 1

ins = my_gen(end=10)
for item in ins:
    print(item)
