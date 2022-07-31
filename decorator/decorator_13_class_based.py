class MyDecorator():
    def __init__(self, number):
        self.number = number

    def __call__(self, func):
        def inner_function(*args, **kwgs):
            for i in range(self.number):
                func(*args, **kwgs)
        return inner_function

@MyDecorator(2)
def my_functioin(name):
    print(name)

my_functioin('amir hossein')
