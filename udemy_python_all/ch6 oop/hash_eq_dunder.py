class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __key(self):
        return (self.name, self.age, self.address)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented

    def __len__(self):
        return self.age

    def __str__(self):
        return f'{self.name} is now {self.age} years old and living in {self.address}.'

    def __repr__(self) -> str:
        return f'name : {self.name}, age : {self.age}, address : {self.address}.'

    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented


robot1 = Robot('Wilson', 30, 'Taiwan')
robot2 = Robot('Grace', 20, 'UK')
print(robot1 == robot2)
print(len(robot1))
print(robot1)  # = str(robot1)
print(str(robot1))
print(repr(robot1))
print(robot1 + robot2)
print(robot1 > robot2)
