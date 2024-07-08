#filter  , map and reduce are the paradigms of the functionl programming
#map and filter come built in with python (in the built in function)

# its filter the given sequence with the healp of a each function that test each element
#in the sequence to be true or not
#syntax :filter (function ,itrable)
#function : test if each element of sequence is true or false
#sequence/itrable: sequence which needs to be filterd ,it can se, lest or tuple
#containers of any itrable
#filter pass each element in the etrable through function and returns only the 
#onse evelaute true

# def checkeven(number):
#   if number % 2 == 0:
#     return True 
#   return False

# def main():
#   evenfilter = filter(checkeven, [1, 2, 3, 4, 5, 6, 7, 8])
#   output = tuple(evenfilter)
#   print('after filter:', output)

# if __name__ == "__main__":
#   main()

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    print(even_numbers)


if __name__ == "__main__":
    main()

