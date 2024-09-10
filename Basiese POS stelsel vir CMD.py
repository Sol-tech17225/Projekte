# Function to add an item to the list
def add_item_to_list(lst, item, price):
    lst.append((item, price))

# Function to display the list of items
def display_list(lst):
    total = 0
    for item, price in lst:
        print(f"{item}   R{price:.2f}")
        total += price
    print("---------------")
    print(f"Total R{total:.2f}")

# Function to clear the list
def clear_list(lst):
    lst.clear()

# Main program that manages the POS system
def pos_system():
    items = []
    while True:
        print("Choose operation:")
        print("1. Add item")
        print("2. Display list")
        print("3. Clear list")
        print("4. Exit")

        # Get the user's choice
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            item = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            add_item_to_list(items, item, price)
        elif choice == '2':
            display_list(items)
        elif choice == '3':
            clear_list(items)
            print("List has been cleared.")
        elif choice == '4':
            print("Exiting the POS system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main program
pos_system()
