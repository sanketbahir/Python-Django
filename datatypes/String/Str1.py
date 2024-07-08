# String is a sequence of charater enclosed in a singel quote/double qoute and tripple quote wue use triple quote in multiline

#Creating a string


institute_name = 'hematite infotech'
instatute_address = "chandan nagar"

print('type of the object', type(institute_name))
print('len of the object',len(institute_name))

print('Access of the 0th position', institute_name[0])#H
print('Access of the 1th position', institute_name[1])#e
print('Access of the 2th position', institute_name[2])#m
print('Access of the 3th position', institute_name[3])#a
print('Access of the 4th position', institute_name[4])#t
print('Access of the 5th position', institute_name[5])#i
print('Access of the 6th position', institute_name[6])#t
print('Access of the 7th position', institute_name[7])#e
print('Access of the 8th position', institute_name[8])#space
print('Access of the 9th position', institute_name[9])#I

print('slicing', institute_name[2:8])
print('slicing', institute_name[-15:-9])

#its a immutable object

#concatenation of the string:
student_name = "sanket"
student_fee = 15000
pending_fee =50.50

Fee_Infromation = student_name +' '+'has to pay '+str(pending_fee)
print('Statuds of student:',Fee_Infromation)

