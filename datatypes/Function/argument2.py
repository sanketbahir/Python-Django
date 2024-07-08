def areaofcircle(Radious,PI=3.14):
  Formula = Radious*Radious*PI
  return Formula

if __name__=="__main__": #conditional check
  result = areaofcircle(10,3.14)
  print('area of the circle:',result)