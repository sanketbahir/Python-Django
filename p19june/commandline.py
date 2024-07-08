#sys module: this module provode access some variables used or 
#mintained by the interpiter
#and to function that interact strongly with the interpreter.

#command line arguments
#the argument that are given 
import sys
# from sys import *
# from sys import argv
def main():
  print('total number of argument :',len(sys.argv))
  print('Applaction name :',sys.argv[0])#commandline.py
  print('Frist argument  :',sys.argv[1])
  print('second argument :',sys.argv[2])
  print('third argument :',sys.argv[3])


if __name__=="__main__":
  main()
  print('Applaction name :',sys.argv[0])#commandline.py
  print('Frist argument  :',sys.argv[1])
  print('second argument :',sys.argv[2])
  print('third argument :',sys.argv[3])


if __name__=="__main__":
  main()
