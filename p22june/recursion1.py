#repeated (itraction) looping
#recutsion function -a function calling it self is a reaction function

# using while loop
def Display(num):
  count = 0
  while(count < num):
    print('hello world')
    count +=1
Display(4) 

print()

#reaction function
def Display(num):
  if(num>0):
    print('hello world')
    Display(num-1)
Display(4)