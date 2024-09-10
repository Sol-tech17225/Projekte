# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide the first number by the second
# Returns an error message if division by zero is attempted
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to clear the console output
def clear():
    print("\033[H\033[J", end="")  # This clears the console output

# Main function to run the calculator
def calculator():
    while True:
        # Display the menu of operations
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear")
        print("6. Exit")

        # Get the user's choice
        choice = input("Enter choice (1/2/3/4/5/6): ")

        # Perform the chosen operation
        if choice in ['1', '2', '3', '4']:
            try:
                # Get the numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle invalid input
                print("Invalid input. Please enter a number.")
                continue

            # Perform the corresponding calculation and display the result
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            # Clear the console output
            clear()
        elif choice == '6':
            # Exit the calculator
            print("Exiting the calculator.")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Call the main function to start the calculator
calculator()
