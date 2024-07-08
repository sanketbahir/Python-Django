def positiveNumber(number):
  if (number>0):
     return True
  return False
  

def main():
  size = int(input('enteer the size'))
  data_input = []
  print('enter the value:')
  for i in range(size):
   value = int(input())
   data_input.append(value)
  print('user list:',data_input)
  filter_positive = list(filter(positiveNumber,data_input))
  print('filter list:',filter_positive)
if __name__=="__main__":
  main()