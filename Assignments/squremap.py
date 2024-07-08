def square_number(Number):
    return Number ** 2

def mapX(healper_function, data):
    result = []
    for no in data:
        result.append(healper_function(no))
    return result

def main():
    user_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    squared_numbers = mapX(square_number, user_list)
    print('Squares of the numbers:', squared_numbers)

if __name__ == "__main__":
    main()
