expenses = []
while True:
    print("\n===EXPENSES TRACKER===")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Inter your choice")
    # Add Expenses
    if choice == "1":
        name = input("Expenses name: ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        ex = {
            "name": name,
            "amount": amount,
            "category": category
        }
        expenses.append(ex)
        print("Expenses added successfully")
    # View Expenses
    elif choice == "2":
        if expenses == 0:
            print("Not Expenses founded")
        else:
            print("\n All Expenses: ")
            for i, ex in enumerate(expenses, start=1):
                print(f"{i}. {ex['name']} {ex['amount']} TK {ex['category']}" )



