from time import sleep

def delay(func):
    def wrapper(name):

        count = 5
        print('you name will be appear in:')

        while count > 0:

            print('%d second' %count)
            sleep(1)
            count -= 1

        func(name)

    return wrapper

@delay
def greeting(name):
    print('your name is %s' %name)

greeting('hossein')