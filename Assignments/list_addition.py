from sys import argv

def main():
    print('Welcome to:', argv[0])

    if len(argv) == 2:
        if argv[1] == '--U':
            print('Usage: please pass arguments as follows: list1 list2')
            exit()
        if argv[1] == '--H':
            print('Help: This application is used for performing addition of two lists')
            exit()

    if len(argv) != 3:
        print('Invalid number of arguments')
        print('Please use --U flag to get the usage')
        print('Please use --H flag to get the help')
        exit()

    list1 = [int(num) for num in argv[1:]]
    list2 = [int(num) for num in argv[2:]]

    if len(list1) != len(list2):
        print("Error: Lists must have the same length for addition")
        exit()

    result = [list1[i] + list2[i] for i in range(len(list1))]
    print('Addition of two lists is:', result)

if __name__ == "__main__":
    main()
