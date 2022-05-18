def add_welcome(func):

    def wrapper(*args):

        result = func(*args)
        return 'welcome ' + result
        
    return wrapper

@add_welcome
def greeting(name):
    return name

print(greeting('hossein'))