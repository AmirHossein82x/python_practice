class school:
    def __init__(self, name, last_name, score):
        self.name = name
        self.last_name = last_name
        self.score = score
class little(school):
    def __init__(self, name, last_name, score):
        super().__init__(name, last_name, score)

p = little("amir hossein", "ghasemi", 20)
print(p.name)
print(p.last_name)
print(p.score)