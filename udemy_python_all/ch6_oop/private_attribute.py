class Robot:
    def __init__(self, name):
        self.name = name
        self.__age = 25

    def age_setter(self, new_age):
        if new_age > 10 and new_age < 100:
            self.__age = new_age
        else:
            print('Your new age is not valid.')

    def age_getter(self):
        print(self.__age)


robot1 = Robot('ZZZ')
robot1.age_setter(-30)
robot1.age_getter()

# Your new age is not valid.
# 25
