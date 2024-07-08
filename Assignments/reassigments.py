# 1)Write a program to print the sum of the first 10 Natural numbers 
# Output: The sum of the first 10 natural number:55 

sum_of_numbers = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    sum_of_numbers += num

print('The sum of the numbers:', sum_of_numbers)


# 2)Write a program to print a table of a number entered by the user 
# Output: Multiplication of table: 5 

count = int(input('Enter the number: '))
multiplication = count * 5
print('Multiplication of table 5:', multiplication)

# 3)Write a program to find the sum of the digits of a number accepted by the user 
# Input: Enter the number 1234 
# Output: The sum of the digit:10 

number = int(input('Enter the number: '))
strnum = str(number) 
total = 0
for num in strnum:
    digit = int(num) 
    total += digit
print('The sum of the total:', total)

# 4) Write a program to find the product of the digits of a number accepted by the user 
# Input: Enter the number 123 
# Output: The product of the digit:6 

number = int(input('Enter the number: '))
strnum = str(number)  

product = 1

for char in strnum:
    digit = int(char)  
    product *= digit

print('The product of the number:', product)

# 5) Write a program to reverse the number accepted by the user using a while loop 
# Input: Enter the number 123 
# Output: Reverse number:321

num = int(input('Enter the number'))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print('Reversed Number: ' + str(reversed_num))

# 6)Write a program to check whether a given year is a leap year or not 
# Input: Enter the year:2012 
# Output: It is not a Leap year 

def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input('Enter the year: '))

if leapyear(year):
    print('is a Leap year : ',year)
else:
    print('is a Leap year : ',year)

# 7)Write a program to check whether a given number is an even or an odd number 
# Input: Enter Number – 5 
# Output: 5 is an odd number 

oddeven = int(input('Enter the number'))
if(oddeven % 2 == 0):
    print('this is a even number : ', oddeven)
else:
    print('this is a odd number : ', oddeven)

# 8) Write a program to check whether a given number is a prime number or not 
# Input: Enter Number – 5 
# Output: 5 is a prime number 

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input('Enter a number: '))

if is_prime(number):
    print(number, 'is a Prime number')
else:
    print(number, 'is not a Prime number')


# 9) Write a program to calculate the factorial of a given number from the user

def factorial(num):
    if num < 0:
        return 'Factorial is not defined for negative numbers'
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

number = int(input('Enter a number: '))

print('Factorial of', number, 'is', factorial(number))

# 10)Write a program to count the total number of digits in a number  
#  Input: Enter the number:123567 
# Output: 6

def count_digits(num):
    num_str = str(num)
    return len(num_str)

number = int(input('Enter the number: '))

print('Total number of digits in', number, 'is', count_digits(number))

# 11) Write a program to print the cube of all numbers from 1 to a number given by the user 
#  Input: 5 
# Output:  
# 1: 1 
# 2: 4 
# 3: 9 
# 4: 16 
# 5: 25 

def print_cubes(num):
    for i in range(1, num + 1):
        cube = i ** 3
        print(f'{i}: {cube}')

number = int(input('Enter a number: '))
print_cubes(number)

# 13) Write a program to print the first 10 natural numbers in reverse order using while loop 

i = 10

while i >= 1:
    print(i)
    i = i - 1

# 14)Write a program to check whether a number entered is a three-digit number or not. 
#  Input: Enter the number: 12  
# Output: Not a three-digit number

number = int(input('Enter the number: '))

if 100 <= number and number <= 999:
    print('It is a three-digit', number)
else:
    print('Not a three-digit', number)


# 15)Write a program to find the greatest number out of three numbers given by the user 
#  Input: Enter three numbers: 5 6 2 
#  Output: 6 is the greatest number 

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

greatest = num1

if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3

print('the greatest number is', greatest)

# 16)Write a program to find the smallest of the digits of a number accepted by the user  
# Input: Enter three numbers: 5 6 2  
# Output: 2 is the smallest number 

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

smallest = num1

if num2 < smallest:
    smallest = num2

if num3 < smallest:
    smallest = num3

print('the smallest number is', smallest)

# 17) Write a program to check whether a person is a senior citizen or not  
# Input: Enter your age: 65 
# Output: Senior Citizen 

age = int(input('Enter your age: '))

if age >= 60:
    print('Senior Citizen')
else:
    print('Not a Senior Citizen')

# 18) Write a program for checking whether a character is a vowel or consonant  
# Input: Enter the character: u 
# Output: Given character is a vowel 

x = input('Enter the character: ')

vowels = 'aeiouAEIOU'

if x in vowels:
    print('Given character is  vowel')
else:
    print('Given character is consonant')

# 19) Write a program to count vowels or consonants of the given string  
# Input: Enter the string: Python  
# Output: The number of vowels: 1 
# The number of consonants: 5 

string = input('Enter the string: ')

vowels = 'aeiouAEIOU'

count_vowels = 0
count_consonants = 0

alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in string:
    if x in alphabets:
        if x in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

print('The number of vowels:', count_vowels)
print('The number of consonants:', count_consonants)

# 20)Write a program to find the last digit in a number  
# Input: Enter the number:123456 
# Output: The last digit in a given number 123456 = 6 

number = input('Enter the number: ')
digits_list = list(number)
last_digit = digits_list[-1]
print('The last digit in a given number', number, '=', last_digit)


