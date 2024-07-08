#
def FullName(firstname,lastname):
  print('Argument firstname: ',firstname)
  print('Argument firstname: ',lastname)
  print(firstname+" "+lastname)

print('positional argument')  

FullName('sanket','bahir')#positional argument
FullName('bahir','sanket')

FullName(lastname='bahir',firstname='sanket')#keyword argument

#substraction

def sub(num1,num2):
  print('fist argument',num1)
  print('second argument',num2)
  print('substraction',num1-num2)
sub(22,23)#keyword argument
sub(num1 = 23,num2=22)