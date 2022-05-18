def add_element1(func):

    def wrapper():

        result = func()
        result.append('<strong>')
        result.insert(0, "<strong>")
        return "".join(result)

    return wrapper

def add_element2(func):

    def wrapper():

        result2 = func()
        new_list = [result2]
        #print(new_list)
        new_list.append('</i>')
        new_list.insert(0, "<i>")
        
        return new_list
        
    return wrapper

@add_element1
@add_element2
def introduction():
    return 'this is a basic program'

#add_element1(add_element2(introduction()))
print(introduction())