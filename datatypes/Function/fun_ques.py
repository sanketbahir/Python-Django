def count_num(data_input,searched):
  count=0
  for i in data_input:
    if(i==searched):
      count +=1
  return count

def main():
  size = int(input('enter the size of the list'))
  data_input = []
  print('inter the value ')
  for i in range(size):
    value = int(input())
    data_input.append(value)
  print('user list:',data_input)


  search_number= int(input('Enter the number you want to be searched'))

  print(search_number,'is repeting ',count_num(data_input,search_number))

if __name__=="__main__":
  main()