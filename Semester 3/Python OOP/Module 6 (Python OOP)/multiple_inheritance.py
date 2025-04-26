# Multiple Inheritance means a class can inherit from more than one parent class.
class Family:
    def __init__(self, address):
        self.address = address

class School:
    def __init__(self, id, level):
        self.id = id
        self.level = level

class Sports:
    def __init__(self, game):
        self.game = game

# Child class inheriting from Family, School and Sports
class Students(Family, School, Sports):
    def __init__(self, address, id, level, game):
        Family.__init__(self, address)
        School.__init__(self, id, level)
        Sports.__init__(self, game)
    def __repr__(self):
        return f'Lives in {self.address}, id is {self.id} at level {self.level} and plays {self.game}'


rifat = Students('Dhaka', 201, 10, 'Cricket')
print(rifat)
