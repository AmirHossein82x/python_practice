def check_name(func):

    def wrapper(*args):
        try:
            if args[0] == 'ali':
                func(args)
            else:
                print('you can not use this program %s' %args[0])
        except IndexError:
            print('you must enter 1 name!')        

    return wrapper

@check_name
def enter_name(name):
    print('welcome to the program %s' %name)

enter_name("ali")
print()
print('--------------------\n')

enter_name("hossein")
print()
print('--------------------\n')

enter_name()
print()
print('--------------------\n')