#reduce  need to be imroved as is resides in  the funcrool modulw 
#reduce()
#functoolse. reduce(function,ittrable,intializer)
#applay function of two argument cumulatively to the item sequence
#son as to reduce the sequence to a single value

from functools import reduce
def addition(number1,number2):
  return number1+number2

def main():
  size = int(input('enter the size:'))
  data_input = []
  print('inter the value:')
  for i in range(size):
    value = int(input())
    data_input.append(value)
  print('user list:',data_input)
  reduce_value = reduce(addition,data_input)
  print('reduce value:',reduce_value)
if __name__=="__main__":
  main()
