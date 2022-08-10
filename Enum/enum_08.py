class MetaClass(type):
    
    def __new__(cls, name, bases, dct):
        instance = super().__new__(cls, name, bases, dct)
        props = list(filter(lambda x: not x.startswith('__'), instance.__dict__))
        # print(props)

        for item in props:
            value = getattr(instance, item)
            setattr(instance, item, instance(name=item.lower(), value=value))
        return instance


class MyEnum(metaclass=MetaClass):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Shape(MyEnum):
    RECTANGLE = 'rec'
    TRIANGLE = 'tri'
    CIRCLE = 'cir'

print(Shape.RECTANGLE.name)
