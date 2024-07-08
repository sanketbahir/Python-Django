def Addition(A,B):
  return A+B

def ReduceX(healper_function,data):
  ans = 0
  for no in data:
    ans = healper_function(ans,no)
    return ans

def main():
  user_list = [2,3,4,5,6,7,8,9,10]
  ReduceList = ReduceX(Addition,user_list)
  print('After Reduce:',ReduceList)
if __name__=="__main__":
  main()