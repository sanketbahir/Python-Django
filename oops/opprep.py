class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def DisplayInfo(self):
        print(f'Name: {self.name} and age: {self.age}')

s1 = Student('Sanket', 22)
s1.DisplayInfo()