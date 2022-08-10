from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def move():
        pass

    @abstractmethod
    def eat():
        pass

class Bird(Animal):
    def eat(self):
        print('I can eat ')

    def move(self):
        print('I can move')
 

#animal = Animal()
""" 
when we use ABC we can not create a instance of Animal in the program
The move and eat function must be created in the child(Bird) class
"""
bird = Bird()
bird.eat()
