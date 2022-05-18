def register(func):

    def wrapper(*args):

        print('before Execution')

        func(*args)

        print('after Excecution')

    return wrapper

@register
def greeting(name):
    print(f'how are you {name}?')

a = greeting('hossein')