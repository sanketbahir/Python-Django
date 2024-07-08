# #lambda function
# #the lambda function is a anonymous function means that function without name
# #as we already  know that the def key word is use to define the a normal function
# #similary , the lambda key word is use to define a anonymus function
# #this function can have number of arguments but only one expration
# #eveluated and reaturned
# #syntax :lambda arguments :expression

def Adation(a,b,c):
  return a+b+c
print('Addition:',Adation(10,12,12))

print()

#lambda function

addfunction = lambda A,B,C : A+B+C
ans = addfunction(10,2,10)
print('using lambda:',ans)
print('type:',type(addfunction))
print()
print('squre of the list:')
num = [2,4,6,8]
squre_number =[]
for i in num:
  lam_squre = lambda i :i**2
  squre_number.append(lam_squre(i))
print('using lamvda function:',squre_number)

multip = lambda A,B,C : A*B*C
reasult = multip(2,2,2)
print(reasult)