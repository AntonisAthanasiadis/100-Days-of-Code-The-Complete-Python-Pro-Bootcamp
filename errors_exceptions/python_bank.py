balance = 100

while True:
    print(f"\nCurrent Balance: €{balance:.2f}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "3":
        print("Thank you for using Python Bank. Goodbye!")
        break

    if choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue

    try:
        amount_str = input("Enter amount: €")
        amount = float(amount_str)

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if choice == "1":
            balance += amount
            print(f"Deposit successful! Deposited: €{amount:.2f}")

        elif choice == "2":
            if amount > balance:
                raise ValueError("Insufficient funds!")
            balance -= amount
            print(f"Withdrawal successful! Withdrew: €{amount:.2f}")

    except ValueError as e:
        print(f"Transaction Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")