# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def DisplayInfo(self):
#         print(f'Name:{self.name} and Age:{self.age}')
# s1 = student('sanket',22)
# s1.DisplayInfo()

class Dog:
    def __init__(self, animal, color, features):
        self.animal = animal
        self.color = color
        self.features = features

    def DisplayChar(self):
        print(f'{self.animal}, {self.color}, {self.features}')

    def ModifyInfo(self):
        print(f'{self.animal}, {self.color}, {self.features}')

x1 = Dog('Dog', 'yellow', 'proctating')
x1.DisplayChar()
s1 = Dog('cat','narangi','wast time and money')
s1.ModifyInfo()