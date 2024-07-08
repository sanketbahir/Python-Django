#function is a block of code wich is used to perfom specific code 
#functions are re useable piceses of progam

#the ALLOW YIU TO GAIVE A NAME TO BOLCK OF STATEMENT,ALLOWING YOU TO RUN THAT
#th eblock using spacific name aneayr in your program of any number of items 
#known as colling a fiun ction defunction colled paramitarise function
#where values youb supplay in the function call are called arguments
def addtion():
  print('no paramiter , no function, no return')
  print('inside addtion')


def addtionX(value1):
  print('1 paramiter,1argument,no returen')
  print('inside Addtion program value1 is:',value1)

def addtionY(value1,value2):
  print('2 paramiter,2 argumint, 1return')
  print('inside  addtion prigram value 1 is ',value1,value2)
  return value1+value2

addtion()
print('_'*50)
addtionX(12)
print('_'*50)
print('add of two numder',addtionY(3j,34))
print('_'*50)
ressult = addtionY(23,24)

print(ressult)