numbers = [8, 21, 4, 45, 66, 93, 5]

for number in numbers:
    if number % 2 != 0:
        print(number)

print('_'*50)

number = [10, 7, 55, 23, 46, 56, 87, 29, 25]
index = 0

while index < len(number):
    if number[index] % 2 != 0:
        print(number[index])
    index += 1
