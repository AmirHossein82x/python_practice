import time

def check_time(func):

    def wrapper():

        func()
        print(time.perf_counter())

    return wrapper

@check_time
def call():

    print('time of performing this function is: ', end="")

call()