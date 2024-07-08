class Student:
    Graduation = 'Bca'
    def graduation_in(cls):
        print('graduation',cls.Graduation)

Student.graduation = classmethod(Student.graduation_in)
Student.graduation()

print()

class Student:
    graduation = 'Bca'
    @classmethod
    def graduation_in(cls):
        print('graduation',cls.graduation)

Student.graduation_in()
