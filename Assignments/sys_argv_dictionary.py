from sys import *

def main():
    print('Welcome to :', argv[0])  # Command info

    if len(argv) != 6:
        print("Invalid number of arguments")
        print("Usage: python script_name.py <name> <age> <city> <job> <salary>")
        return

    my_dictionary = {'name': argv[1], 'age': argv[2], 'city': argv[3], 'job': argv[4], 'salary': argv[5]}
    
    for key, value in my_dictionary.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == "__main__":
    main()