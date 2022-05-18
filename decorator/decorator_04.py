def print_value(func):

    def wrapper(*args, **kwargs):

        if len(args) != 0:
            joined = ','.join(map(str, args))
            print(f'your inputs are: {joined}')

        if len(kwargs) != 0:

            for key, value in kwargs.items():
                print(f'your inputs are: {key} : {value} ')

        func(*args, **kwargs)
        result1, result2 = func(*args, **kwargs)
        print('your out put is: ', end="")
        print(','.join(map(str,result1)))

        print('your out put is: ', end='')
        for key, value in result2.items():
            print("%s : %d" % (key, value))

    return wrapper



@print_value
def double(*args, **kwargs):

    new_args = list(map(lambda x: x * 2, args))

    for key, value in kwargs.items():
        kwargs[key] = value * 2
        
    return new_args, kwargs

double(1, 2, 3, 4, a=5)


