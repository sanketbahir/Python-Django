#creating the list
#same data types / homogenus
courses = ['python','java','php','angular']
student_id = [123,124,125,126]
temperature = [45.7,35.6,36.6]

#mixed_data type/heterterogenus
mixed_data = [124,'sanket bahir',2.5,True,124]
print('mixed  data type list:',mixed_data)
print('data type:',type(mixed_data))

#index -> is ude to access values
mixed_data = [124,'sanket bahir',2.5,True,124]
#positive index

print ('Access oth position:',mixed_data[0])#124
print ('Access 1th position:',mixed_data[1])#124
print ('Access 2th position:',mixed_data[2])#124
print ('Access 3th position:',mixed_data[3])#124
print ('Access 4th position:',mixed_data[4])#124

print('--------------------------------------------')

print ('Access -1th position:',mixed_data[-1])#124
print ('Access -2th position:',mixed_data[-2])#124
print ('Access -3th position:',mixed_data[-3])#124
print ('Access -4th position:',mixed_data[-4])#124
print ('Access -5th position:',mixed_data[-5])#124


#slicing : Access the element from a specific [start:stop(exclude)]

print('Access values using sclicing:', mixed_data[:])
print('Access values using scliceing', mixed_data[1:3])
print('Access values using scliceing', mixed_data[2:])

#negitive
print('Access values using scliceing', mixed_data[-4:-1])