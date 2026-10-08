# Personal Mini-Toolkit
# This program provides three simple tools through a menu.


# Tool 1: Simple Calculator
# This tool performs basic arithmetic operations on two numbers.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = first_number + second_number
            print(f"Your answer is {result}.")

        elif operation == "2":
            result = first_number - second_number
            print(f"Your answer is {result}.")

        elif operation == "3":
            result = first_number * second_number
            print(f"Your answer is {result}.")

        elif operation == "4":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = first_number / second_number
                print(f"Your answer is {result}.")

        else:
            print("That is not a valid operation.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: Shopping List
# This tool allows the user to add, view, and remove shopping items.
def shopping_list_tool():
    shopping_list = []

    while True:
        print("\n--- Shopping List ---")
        print("1. Add item")
        print("2. Show list")
        print("3. Remove item")
        print("4. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter the item to add: ").strip()

            if item:
                shopping_list.append(item)
                print(f"{item} has been added to your shopping list.")
            else:
                print("Please enter an item.")

        elif choice == "2":
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                print("\nYour shopping list:")

                for item in shopping_list:
                    print(f"- {item}")

        elif choice == "3":
            item = input("Enter the item to remove: ").strip()

            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from your shopping list.")
            else:
                print(f"{item} is not on your shopping list.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Please choose a valid option from 1 to 4.")


# Tool 3: Even or Odd Checker
# This tool checks whether a number is even or odd.
def even_odd_checker():
    print("\n--- Even or Odd Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Main menu
# This loop keeps the toolkit running until the user chooses Quit.
print("========================================")
print("       WELCOME TO MY MINI-TOOLKIT")
print("========================================")
print("Enjoy using the tools!")

while True:
    print("\n========================================")
    print("1. Simple Calculator")
    print("2. Shopping List")
    print("3. Even or Odd Checker")
    print("4. Quit")
    print("========================================")

    choice = input("Choose a tool: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        shopping_list_tool()

    elif choice == "3":
        even_odd_checker()

    elif choice == "4":
        print("\nThank you for using My Mini-Toolkit!")
        print("Goodbye and have a great day!")
        break

    else:
        print(f"Sorry, '{choice}' is not on the menu.")
        print("Please choose an option from 1 to 4.")