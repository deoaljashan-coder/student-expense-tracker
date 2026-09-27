import datetime
import os

FILE_NAME = "expenses.txt"

def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, amount, date = line.strip().split(",")
                expenses.append({"name": name, "amount": float(amount), "date": date})
    return expenses

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        for exp in expenses:
            f.write(f"{exp['name']},{exp['amount']},{exp['date']}\n")

def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    date = datetime.date.today()
    expenses.append({"name": name, "amount": amount, "date": str(date)})
    save_expenses(expenses)
    print("Expense added successfully!\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- Expense List ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']} on {exp['date']}")
    print()

def total_expenses(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ₹{total}\n")

def main():
    expenses = load_expenses()
    while True:
        print("===== Student Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
