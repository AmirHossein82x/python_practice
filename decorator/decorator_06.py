from time import sleep

def delay(func):

    def wrapper(name):
        
        sleep(5)
        func(name)

    return wrapper

@delay
def greeting(name):
    print('how are you doing %s?' %name)

greeting('hossein')