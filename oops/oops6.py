#not defined inside any method 
class Student:
    graduation = 'BCA'
    
    def __init__(self, name, course):
        self.name = name
        self.course = course

obj1 = Student('sanket', 'python')
print(obj1.graduation)
