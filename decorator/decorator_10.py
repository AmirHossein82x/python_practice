def decorator(*args):

    def register(func):
        
        def wrapper(*a):

            print(args[0])
            func(*a)
            print(args[1])
   
        return wrapper

    return register

@decorator('before', 'after')
def say_hello(name):
    print('hello %s' %name)

say_hello('hossien')