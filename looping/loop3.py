#Dynamic input
def main():
  size = int(input('Enter the size of the list'))
  Data_input=[]
  print('Enter the value:')
  for i in range(size):
    value = int(input())
    Data_input.append(value)
  print('list from the user:',Data_input)
if __name__=="__main__":
  main()