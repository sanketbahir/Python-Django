#built in module  (random)
#random madule generates random numbers 
#write a program which will generate  random password
#->aphapet -3,number=1,symboles =2 ==> password =a@BN2$
import random

#choise it reatun an a random element 
coures = ['python','java','anguler','react']
print(random.choise(coures))

#shuffle => it will give me randonm number order
ice_cream = ['vanilla','Blueberry','choco-chips']
shuffel= random.shuffel(ice_cream)
print('shuffel:'ice_cream)

#random -> random number between 0 to 1
print(random.random())

#randrange -> return a number between given numbers
print(random.randorange(2,10))

#randint
print(random.randint(2,9)) #both include