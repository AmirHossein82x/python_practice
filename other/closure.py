def multiplier(n):

    def wrapper(x):
        return n * x

    return wrapper

multiply_by_3 = multiplier(3)
print(multiply_by_3(10))


