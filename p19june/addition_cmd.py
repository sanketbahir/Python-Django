from sys import argv

def addition(A, B):
    Ans = 0
    Ans = A + B
    return A + B 

def main():
    print('Welcome to :', argv[0])  # Addition command

    if len(argv) == 2:
        if argv[1] == '--U':
            print('Usage: please pass arguments as follows: Name_of_first_number')
            exit()
        if argv[1] == '--H':
            print('Help: This application is used for performing addition of two numbers')
            exit()
    if len(argv) != 3:
        print('Invalid number of arguments')
        print('Please use --U flag to get the usage')
        print('Please use --H flag to get the help')
        exit()
    
    Result = addition(int(argv[1]), int(argv[2]))
    print('Addition is:', Result)

if __name__ == "__main__":
    main()
