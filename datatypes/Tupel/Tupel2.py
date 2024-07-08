#packing and Unpanking
emp_details = (124,'sanket',18000,True) #paking all values
(id,nmae,salary,is_available)= emp_details #unpacking
#extracting all values from a variable

print(id)
print(is_available)

emp_details = (124,'sanket',18000,True,'Trainer','Developer',45)
(id,name,is_available,*jobrole)= emp_details
print(jobrole)
