import calculator_module

def multi(value1, value2):
    result = calculator_module.multi(value1, value2)
    print(f'The multiplication of {value1} and {value2} is: {result}')

def div(value1, value2):
    result = calculator_module.div(value1, value2)
    print(f'The division of {value1} by {value2} is: {result}')

def sub(value1, value2):
    result = calculator_module.sub(value1, value2)
    print(f'The subtraction of {value2} from {value1} is: {result}')

def add(value1, value2):
    result = calculator_module.add(value1, value2)
    print(f'The addition of {value1} and {value2} is: {result}')

def main():
    value1 = int(input('Enter the first number: '))
    value2 = int(input('Enter the second number: '))

    multi(value1, value2)
    div(value1, value2)
    sub(value1, value2)
    add(value1, value2)

if __name__ == "__main__":
    main()
