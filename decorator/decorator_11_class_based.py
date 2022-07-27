class AgeValidation:
    def __init__(self, data):
        self.data = data
        self.key = 'age'
    
    def __call__(self, *args, **kwds):
        res = self.data.get(self.key)
        if 1 <= res <120:
            print(True)
        else:
            print(False)

class ScoreValidation:
    def __init__(self, data):
        self.data = data
        self.key = 'score'
    
    def __call__(self, *args, **kwds):
        res = self.data.get(self.key)
        if 0 <= res <= 20:
            print(True)
        else:
            print(False)

data = {'score':19, 'age': 18}

age = AgeValidation(data)
age()

score = ScoreValidation(data)
score()