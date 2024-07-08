import arithmatic

print('Choose operators \n1. Addition \n2. Subtraction')
select = int(input('Select 1/2: '))
print(select)

def main():
    value_01 = int(input('Enter the first number: '))
    value_02 = int(input('Enter the second number: '))
    if select == 1:
        ans = arithmatic.Addition(value_01, value_02)
        print(f'Addition of {value_01} and {value_02}: {ans}')
    elif select == 2:
        ans = arithmatic.Subtraction(value_01, value_02)
        print(f'Subtraction of {value_01} and {value_02}: {ans}')
    else:
        print('Please select 1 or 2')

if __name__ == "__main__":
    main()
