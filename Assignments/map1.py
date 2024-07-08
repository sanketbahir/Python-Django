#map() functionn returns a amp object (which is an itrate) fo the result after
#applying the given function to each item of a given itrable(list tupel etc)

#or

#allows you to process and transfrom all the item in itrable using an
#syntax : map(function,itrable,[itrable1,itrable2...])
#using list : [2,3,6,9,1]-->[4,9,36,9,81,1]

def square(number):
    return number * number

def main():
    size = int(input('Enter number of elements: '))
    data_input = []
    print('Enter values:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User list:', data_input)
    map_square = list(map(square, data_input))
    print('Mapped list:', map_square)

if __name__ == "__main__":
    main()

