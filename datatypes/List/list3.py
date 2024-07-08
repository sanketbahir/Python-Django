#Methods:
# append method ->will add element at last
student_name = ['sanket','keten']
student_name.append('arpita')
print('Append method',student_name)

#Extend method -> it wil add element of list (or iterable) to the list
student_name.extend(['arpita','pooja','rahul'])
print(student_name)

#Insert() - adds an element at the specified position
ice_cream = ['vanila','choco-chips']
ice_cream.insert(1,'chapati')
print(ice_cream)

#remove (removes the specified value)
courses = ['python','java','php','.net']
courses.remove('.net')
print(courses)

#pop() (removes the value of specifaction position)
emp_name = ['kasturi','shubham','Aadesh']
emp_name.pop(1)
print('pop method shubhum:',emp_name)

