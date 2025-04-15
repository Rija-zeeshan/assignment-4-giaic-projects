# Function to access an element at a specific index
def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."

# Function to modify an element at a specific index
def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return "Element updated successfully."
    else:
        return "Index out of range."

# Function to slice a list from start to end index
def slice_list(my_list, start, end):
    if start < 0 or end > len(my_list) or start > end:
        return "Invalid indices."
    return my_list[start:end]

# Game to interact with the list
def index_game():
    # Sample list
    items = ['red', 'blue', 'green', 'yellow', 'purple']

    while True:
        print("\nYour list:", items)
        print("Choose an operation: access / modify / slice / quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "access":
            idx = int(input("Enter index to access: "))
            print("Result:", access_element(items, idx))

        elif choice == "modify":
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print(modify_element(items, idx, new_val))

        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(items, start, end)
            print("Sliced List:", result)

        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the index game
index_game()
