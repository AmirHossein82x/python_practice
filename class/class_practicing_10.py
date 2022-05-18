class Duck:

    def walk(self):
        print('this duck is walking')

    def talk(self):
        print('this duck is qwuacking')

class Chicken:

    def walk(self):
        print('this chicken is walking')

    def talk(self):
        print('this chicken is clucking')

class Person():
    
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('you caught the critter!')

duck = Duck()
chiken = Chicken()
person = Person()

#person.catch(duck)
person.catch(chiken)


