def run_twice(func):

    def wrapper():
        print('before call ...')
        func()
        func()
        print('after call ...')

    return wrapper

@run_twice
def say_greeting():
    print('hello how are you')

say_greeting()





#def run(func):
#    def a():
#        func()
#
#    return a
#
#@run
#def day():
#    print('ki')
#
#day()
