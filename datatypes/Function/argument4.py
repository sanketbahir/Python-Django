#docstring :the first string after the function is called the string
#it is used to describe the functionality of the function
#optional(but consider for a good reason)

def areaofcircle(Radious,PI=3.14):
  '''claculating the area of circle using keyword argument and second value as a deafult paramiter set on 3.14'''
  Formula = Radious*Radious*PI
  return Formula

def main():
  print('keyword argument')
  result = areaofcircle(PI=3,Radious=10)
  print('area of the circle:',result)#10*10*3
  print('first argument keyword and second argument is default')
  result = areaofcircle(Radious=10)
  print('area of the circle:',result)#10*10*3.14


if __name__=="__main__": #conditional block
 main()