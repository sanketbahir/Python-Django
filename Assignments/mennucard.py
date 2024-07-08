fruit = ['apple', 'mango', 'orange', 'lemon']

def display_fruit():
        print(f"{fruit_name} is available.")
   

def add_fruit():
    fruit_name = input("Enter the name of the fruit to add: ")
    fruit.append(fruit_name)
    print(f"{fruit_name} has been added to the list.")
    print("Current fruit list:", fruit)

def delete_fruit():
    fruit_name = input("Enter the name of the fruit to delete: ")
    if fruit_name in fruit:
        fruit.remove(fruit_name)
        print(f"{fruit_name} has been removed from the list.")
    else:
        print(f"{fruit_name} is not in the list.")
    print("Current fruit list:", fruit)

def update_fruit():
    old_name = input("Enter the name of the fruit to update: ")
    if old_name in fruit:
        new_name = input("Enter the new name of the fruit: ")
        fruit[fruit.index(old_name)] = new_name
        print(f"{old_name} has been updated to {new_name}.")
    else:
        print(f"{old_name} is not in the list.")
    print("Current fruit list:", fruit)

def main():
    print("\nMenu:")
    print("1. Check if a fruit is available")
    print("2. Add a fruit")
    print("3. Delete a fruit")
    print("4. Update a fruit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_fruit()
    elif choice == '2':
        add_fruit()
    elif choice == '3':
        delete_fruit()
    elif choice == '4':
        update_fruit()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
