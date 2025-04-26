from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod  # Forces all subclasses to implement the 'eat' method
    def eat(self):
        print('I need food')

    def move(self):
        print("Douraaaaaaaa")  # Default implementation of move (can be overridden)

# Concrete subclass
class Monkey(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__()

    # Since 'eat' is abstract in the base class, this method MUST be implemented
    def eat(self):
        print(f'Hi I am {self.name}, I am eating banana')

    # Overriding 'move' is optional; if not overridden, base class version will be used
    def move(self):
        print('Hanging on the tree')

# Creating an instance of Monkey and calling its methods
mnky = Monkey('Mumma Miya')
mnky.eat()
mnky.move()

# You can't do this:
# a = Animal()  # ❌ This will raise an error because abstract classes can't be instantiated
