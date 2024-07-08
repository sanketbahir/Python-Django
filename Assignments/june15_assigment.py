from functools import reduce

# Function 1: Power of Two
def power_of_two(x):
    return x ** 2

# Function 2: Multiplication
def multiply(x, y):
    return x * y

# Function 3: Filter for numbers between 70 and 90
def positiveNumber(num):
    return num >= 70 and num <= 90

# Function 4: Filter for even numbers
def filter_even_numbers(num):
    return num % 2 == 0

# Function 5: Map to increase each number by 10
def increase_by_10(num):
    return num + 10

# Function 6: Map to calculate cube
def calculate_cube(num):
    return num ** 3

# Function 7: Reduce to return product of all numbers
def multiply_numbers(number1, number2):
    return number1 * number2

# Main function
def main():
    # 1. Power of Two
    input_value = int(input('Enter a number for power of two calculation: '))
    output_value = power_of_two(input_value)
    print('1. Input:', input_value, 'Output:', output_value)

    # 2. Multiplication
    num1 = int(input("Enter the first number for multiplication: "))
    num2 = int(input("Enter the second number for multiplication: "))
    output_value = multiply(num1, num2)
    print("2. Output:", output_value)

    # 3. Filter for numbers between 70 and 90
    size = int(input('Enter the size for filtering: '))
    data_input = []
    print('Enter values for filtering:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User list for filtering:', data_input)
    filter_positive = list(filter(positiveNumber, data_input))
    print('3. Filtered list (between 70 and 90):', filter_positive)

    # 4. Filter for even numbers
    size = int(input('Enter the size for filtering even numbers: '))
    data_input = []
    print('Enter values for filtering even numbers:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User list for filtering even numbers:', data_input)
    filtered_even_numbers = list(filter(filter_even_numbers, data_input))
    print('4. Filtered list (even numbers):', filtered_even_numbers)

    # 5. Map to increase each number by 10
    size = int(input('Enter the size for mapping increase by 10: '))
    data_input = []
    print('Enter values for mapping increase by 10:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User list for mapping increase by 10:', data_input)
    map_increase = list(map(increase_by_10, data_input))
    print('5. Mapped list (increased by 10):', map_increase)

    # 6. Map to calculate cube
    size = int(input('Enter the size for mapping cubed: '))
    data_input = []
    print('Enter values for mapping cubed:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User list for mapping cubed:', data_input)
    mapped_cube = list(map(calculate_cube, data_input))
    print('6. Mapped list (cubed):', mapped_cube)

    # 7. Reduce to return product of all numbers
    size = int(input('Enter the size for reducing: '))
    data_input = []
    print('Enter values for reducing:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User list for reducing:', data_input)
    reduce_value = reduce(multiply_numbers, data_input)
    print('7. Reduced value (product):', reduce_value)

if __name__ == "__main__":
    main()
