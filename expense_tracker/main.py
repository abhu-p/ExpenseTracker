while True:
    print("Welcome to Expense Manager")
    print()

    print("Choose an option")
    print("1. Add an expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Add item's name: ")
        price = input("Add price: ")

        with open("expenses.txt", "a") as file:
            file.write(f"{name} - Rs.{price}\n")

        print("Expense added successfully.")

    elif choice == "2":
        print("\nYour Expenses:\n")
        try:
            with open("expenses.txt", "r") as file:
                data = file.read()
                if data == "":
                    print("No expenses.")
                else:
                    print(data)
        except FileNotFoundError:
            print("No expenses recorded.")

    elif choice == "3":
        print("Exiting!")

        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
