class Human:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}"

eve = Human('eve', None, None)
adam = Human('adam', None, None)

habil = Human('habil', adam, eve)
ghabil = Human('ghabil', adam, eve)
marry = Human('marry', adam, eve)

print(habil.mother)