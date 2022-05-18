def arrange(*args):
    sum = 0
    for i in range(len(args)):
        sum += int(i)
    return sum
print(arrange(1, 2, 3, 4))

def arrange(*args):
    sum = 0
    for i in args:
        sum += int(i)
    return sum
print(arrange(1, 6, 9, 7))

def udemi(**kwargs):
    for key, value, in kwargs.items():
        print('%s: %s' %(key, value))

udemi(a = "aki", b = 'hossein')