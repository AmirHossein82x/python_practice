def my_gen():
    a = 1
    print(f"my a is {a}")
    yield a

    a = 2
    print(f"my a is {a}")
    yield a

    a = 3
    print(f"my a is {a}")
    yield a

    a = 4
    print(f"my a is {a}")
    yield a

my_genarator = my_gen()
print(my_genarator)
print('------------------------------------')

#print(next(my_genarator))
#print(next(my_genarator))
#print(next(my_genarator))
#print(next(my_genarator))
for item in my_genarator:
    print(item)
    