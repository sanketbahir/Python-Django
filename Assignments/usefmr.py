def check_even(Number):
  return Number%2 ==0

def filterX(healper_function,data):#healper_function = checkeven , data = user_list
    result = []
    for no in data:
      if(healper_function(no)==True):#checkeven (no) --> function call
        result.append(no)
    return result

def main():
  user_list = [2,3,4,5,6,7,8,9,10]
  filtereven=filterX(check_even,user_list) #function call
  print('after filterning even number:',filtereven)

if __name__=="__main__":
  main()

  