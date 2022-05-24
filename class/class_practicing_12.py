class Mother:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}"

class Father:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}"

class Child:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}"


eve = Mother("eve", None, None)
adam = Father('adam', None, None)

print(eve)
print(adam)

habil = Child('habil', adam, eve)
ghabil = Child('ghabil', adam, eve)

print(habil)
print(ghabil)
print(habil.father)