#1. Write a program which contains one lambda function which accepts one parameter
#and return power of two
#Ex: Input:4 Output: 16

def power_of_two(x):
    return x ** 2

def calculate_power(input_value):
    return power_of_two(input_value)

input_value = int(input('Enter a number: '))
output_value = calculate_power(input_value)
print('Input:', input_value, 'Output:', output_value)


#2. Write a program which contains one lambda function which accepts one parameter
#and return its multiplication
#Ex: Input:4  3  Output: 12

multiply = lambda x, y: x * y

def calculate_multiplication(numbers):
    return multiply(*numbers)

def get_input():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return [num1, num2]

input_values = get_input()
output_value = calculate_multiplication(input_values)

print("Output:", output_value)

#3.Write a program which contains filter()
#List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which greater than or equal to 70 and
#less than or equal to 90

def positiveNumber(num):
    return num >= 70 and num <= 90

size = int(input('Enter the size: '))
data_input = []
print('Enter the values:')
for i in range(size):
    value = int(input())
    data_input.append(value)

print('User list:', data_input)
filter_positive = list(filter(positiveNumber, data_input))
print('Filtered list:', filter_positive)

#4.Write a program which contains filter()
#List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which are odd numbers

def filter_even_numbers(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

size = int(input('Enter the size: '))
data_input = []
print('Enter the values:')
for i in range(size):
    value = int(input())
    data_input.append(value)

print('User list:', data_input)
filtered_even_numbers = filter_even_numbers(data_input)
print('Filtered list (even numbers):', filtered_even_numbers)

#5.Write a program which contains map()
#List contains the numbers which are accepted from user.
#map function will increase each number by 10

def increase_by_10(num):
    return num + 10

size = int(input('Enter number of elements: '))
data_input = []
print('Enter values:')
for i in range(size):
    value = int(input())
    data_input.append(value)

print('User list:', data_input)
map_increase = list(map(increase_by_10, data_input))
print('Mapped list (increased by 10):', map_increase)

#6.Write a program which contains map()
#List contains the numbers which are accepted from user.
#map function will calculate its Cube

def calculate_cube(num):
    return num ** 3

size = int(input('Enter number of elements: '))
data_input = []
print('Enter values:')
for i in range(size):
    value = int(input())
    data_input.append(value)

print('User list:', data_input)
mapped_cube = list(map(calculate_cube, data_input))
print('Mapped list (cubed):', mapped_cube)

#7.Write a program which contains reduce()
#List contains the numbers which are accepted from user.
#reduce will return product of all numbers
from functools import reduce

def multiply(number1, number2):
    return number1 * number2

size = int(input('Enter the size: '))
data_input = []
print('Enter the values:')
for i in range(size):
    value = int(input())
    data_input.append(value)

print('User list:', data_input)
reduce_value = reduce(multiply, data_input)
print('Reduced value (product):', reduce_value)
