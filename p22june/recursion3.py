#addtion using whhile loop

def add(num):
    ans = 0
    while num >= 0:
        ans = ans + num
        num -= 1
    return ans

print('addition using while loop:', add(5))
print()

#addtion using recursion function


def addition(no):
    if no < 0:
        return 0
    else:
        return no + addition(no - 1) #5 +addtion (5-1) =

print('addition using recursion:', addition(5)) 


# find odd numbers using recursion

 num = int(input('Enetr the number : '))

def odd(num):
  if(num % 2 !== 0):
    return 0
  else:
    return while(num % 2 == 0):
