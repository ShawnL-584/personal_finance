class Robot:
    # in classes, we can also define doc string
    '''
    Robot class is for creating a robot
    '''
    ingredient = 'metal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} is walking...')

    def sleep(self, hours):
        print(f'{self.name} is gonna sleep for {hours} hours.')

    def greet(self):
        print(
            f'Hi, My name is {self.name}. I am made of {self.__class__.ingredient}')


robot1 = Robot('Shawn', 30)
robot2 = Robot('Zoe', 33)

print(robot1.name, robot1.age)
print(robot2.name, robot2.age)
robot1.walk()
robot2.sleep(3)
print(robot1.__doc__)
robot1.greet()
print(Robot.ingredient)
print(robot1.ingredient)
print(robot1.__class__.ingredient)
