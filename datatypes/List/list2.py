mixed_data = [124,'sanket bahir',2.5,True,124]
print ('Mixed data:',mixed_data)
del mixed_data[-1]
print('using del removinng last value',mixed_data)
print()
print('mixed data:',mixed_data)
mixed_data[-1]=False
print('replcing value of true',mixed_data)

mixed_data[1]='ketan gosavi'
mixed_data[2]=-89
print(mixed_data)

#Concatenation (+ oprator)
courses = ['python','java']
more_course = ['Php','cloud coumputing','Angular']
print('Concatenation of list:', courses+more_course)