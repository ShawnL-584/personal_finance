class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f'{self.name} is sleeping....')

    def eat(self):
        print(f'{self.name} is eating food')


class Student(People):
    def __init__(self, name, age, student_id):
        # People.__init__(self, name, age)
        super().__init__(name, age)
        self.student_id = student_id

    def eat(self, food):
        print(f'{self.name} is now eating {food}.')


p1 = People('AA', 20)
s1 = Student('BB', 18, 710022)
print(s1.name)
s1.sleep()
s1.eat('chicken')
