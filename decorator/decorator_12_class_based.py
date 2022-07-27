class Decorator1:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        res = self.func(*args, **kwds)
        return 'welcome %s' %res


@Decorator1
def test(name):
    return name

print(test(name = 'ali'))