def numSwap():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    return print(num2,num1)

numSwap()

def numSwap2():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    temp = num1
    a = num2
    b = temp
    return print(a,b)

numSwap2()

def checkDigit(digit):
    if len(str(digit)) != 3:
        print(f'{digit} is not a three-digit number')
    else:
        print(f'{digit} is a three-digit number')

checkDigit(digit = int(input('Enter the number: ')))

def vowelOrConsonant(character):
    chart = character.lower()
    if chart in 'aeiou':
        print(f'{chart} is a vowel')
    else:
        print(f'{chart} is consonant')

vowelOrConsonant(input('Enter the character: '))

def num_of_vowelOrConsonant(character):
    numberOfVowels = 0
    numberOfConsonants = 0
    for char in character.lower():
        if char in 'aeiou':
            numberOfVowels += 1
        else:
            numberOfConsonants += 1
    print(f'The number of vowels: {numberOfVowels}')
    print(f'The number of consonants: {numberOfConsonants}')            

num_of_vowelOrConsonant(input('Enter the character: '))

def reverse_word(chart):
    word = ''
    for x in chart:
        word = x + word
    print(word)

reverse_word(input('Enter a string: '))

def findLastDigit(digit):
    last_digit = digit % 10
    print(f'The last digit is {last_digit}')

digit = int(input('Enter the number: '))
findLastDigit(digit)



