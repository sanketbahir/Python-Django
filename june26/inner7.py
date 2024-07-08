def subtraction(value1,value2):
    Ans = 0
    Ans = value1-value2
    return Ans

def decorated_function(function_name):
    def inner(A,B):
        if(A<B):
            A,B = B,A 
        output = function_name(A,B)

        return output
    return inner

def main():
    value1 = int(input('enter first number : '))
    value2 = int(input('enter second number : '))

    new_function = decorated_function(subtraction)
    Result = new_function(value1,value2)
    print('Sub : ',Result)

if __name__ == '__main__':
  main()