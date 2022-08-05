class Validator:
    def __init__(self, data):
        self.data = data

    def age_validator(self, age):
        if not isinstance(age, int):
            raise TypeError(f'expecteds int but got {type(age).__name__}')

    def validata(self):
        for func_name in filter(lambda x: x.endswith('validator'), dir(self)):
            func = getattr(self, func_name)
            key = func_name.replace('_validator', '')
            return func(self.data.get(key))

data = {'age': '34'}
a = Validator(data=data)
a.validata()        