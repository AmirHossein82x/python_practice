def my_pow(number):
    for i in range(number):
        yield pow(2, i)

instance = my_pow(10)
#print(next(instance))
#print(next(instance))
#print(next(instance))
#print(next(instance))
#print(next(instance))
#print(next(instance))
#print(next(instance))
#print(next(instance))
#print(next(instance))
for number in instance:
    print(number)