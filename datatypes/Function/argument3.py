# def areaofcircle(Radious,PI=3.14):
#   Formula = Radious*Radious*PI
#   return Formula

# def main():
#   print('position argument 10 as a reduis and pi as a 3')
#   result = areaofcircle(10,3)
#   print('area of the circle:',result)#300 -> 10*10*3
#   print()
#   print('position argument 1.3 as a radious and Pi as a 10')
#   result = areaofcircle(3.14,10)
#   print('area of the cricle',result)

# if __name__=="__main__": #conditional check
#  main()

def areaofcircle(Radious,PI=3.14):
  Formula = Radious*Radious*PI
  return Formula

def main():
  print('first argument positional and second argument is default')
  result = areaofcircle(10)
  print('area of the circle:',result)


if __name__=="__main__": #conditional check
 main()