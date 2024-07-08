
numbers = range(1, 11)

sum_of_numbers = sum(numbers)

print('The sum of the first 10 natural numbers:',sum_of_numbers)

print('_'*50)

multi = int(input('Enter the number: '))

def multiplicton():
    return 5 * multi

result = multiplicton()
print('Multiplication of table 5:', result)

print('_'*50)

size = int(input('Enter the size of the list: '))
numbers = []

def main():
    print('Enter the numbers:')
    for i in range(size):
        num = int(input(f'Number {i + 1}: '))
        numbers.append(num)
    
    print('User list:', numbers)
    
    sum_of_all_digits = 0
    for number in numbers:
        total = sum(int(digit) for digit in str(number))
        sum_of_all_digits += total
        print(f'The sum of the digits of {number} is: {total}')
    
    print(f'The sum of all the digits in the list is: {sum_of_all_digits}')

main()

print('_'*50)


number = int(input("Enter the number: "))
original_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10

print(f"Original number: {original_number}")
print(f"Reverse number: {reverse_number}")

print('_'*50)

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

print('_'*50)

def check_even_odd(number):
    if number % 2 == 0:
        return str(number) + ' is an even number'
    else:
        return str(number) + ' is an odd number'

number = int(input('Enter Number: '))

result = check_even_odd(number)

print(result)

print('_'*50)

def check_prime(number):
    if number <= 1:
        return str(number) + ' is not a prime number'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return str(number) + ' is not a prime number'
    return str(number) + ' is a prime number'

number = int(input('Enter Number: '))

result = check_prime(number)

print(result)

print('_'*50)

def calculate_factorial(number):
    if number < 0:
        print("Factorial is not defined for negative numbers")
        return
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")

number = int(input("Enter Number: "))
calculate_factorial(number)

print('_'*50)

number = input("Enter the number: ")
digit_count = len(number)
print(digit_count)

print('_'*50)

n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i, ":", i * i)
    i += 1

print('_'*50)

print("First 10 natural numbers in reverse order:")
i = 10
while i >= 1:
    print(i)
    i -= 1

print('_'*50)

number = input("Enter the number: ")

if len(number) == 3:
    print("A three-digit number")
else:
    print("Not a three-digit number")

print('_'*50)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

max_number = num1
if num2 > max_number:
    max_number = num2
if num3 > max_number:
    max_number = num3

print(max_number, "is the greatest number")

print('_'*50)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

smallest_number = num1
if num2 < smallest_number:
    smallest_number = num2
if num3 < smallest_number:
    smallest_number = num3

print(smallest_number, "is the smallest number")

print('_'*50)

age = int(input("Enter your age: "))

if age >= 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")

print('_'*50)

character = input("Enter the character: ")

if character.lower() in 'aeiou':
    print("Given character is a vowel")
else:
    print("Given character is a consonant")

print('_'*50)

string = input("Enter the string: ")

vowels = 0
consonants = 0

for char in string:
    if char in 'aeiouAEIOU':
        vowels += 1
    elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        consonants += 1

print("The number of vowels:", vowels)
print("The number of consonants:", consonants)

print('_'*50)

word = input("Enter the word: ")

reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print(reversed_word)
