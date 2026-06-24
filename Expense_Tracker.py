import os
import csv
from datetime import datetime

EXPENSES_FILE = "expenses.csv"

CATEGORIES = ["Food", "Transport", "Shopping", "Entertainment", "Other"]


def load_expenses():
    expenses = []
    if not os.path.exists(EXPENSES_FILE):
        return expenses
    with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader is None:
            return expenses
        for row in reader:
            expenses.append(row)
    return expenses


def save_expenses(expenses):
    if not expenses:
        if os.path.exists(EXPENSES_FILE):
            os.remove(EXPENSES_FILE)
        return
    with open(EXPENSES_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["date", "category", "description", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    print("\nAvailable Categories:")
    for i, category in enumerate(CATEGORIES, 1):
        print(str(i) + ". " + category)
    
    while True:
        choice = input("Select category (1-5): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            break
        print("Invalid selection. Please choose a number between 1 and 5.")
    
    description = input("Enter expense description: ").strip()
    
    while True:
        amount = input("Enter amount: ").strip()
        try:
            float(amount)
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"date": date, "category": category, "description": description, "amount": amount})
    save_expenses(expenses)
    print("Expense added successfully.")


def show_total_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    
    total = 0
    for expense in expenses:
        try:
            total += float(expense["amount"])
        except ValueError:
            pass
    
    print("\nTotal Expenses: " + str(total))


def show_expenses_by_category(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\nExpenses by Category:")
    for category in CATEGORIES:
        category_expenses = [e for e in expenses if e["category"] == category]
        if not category_expenses:
            continue
        
        total = 0
        for expense in category_expenses:
            try:
                total += float(expense["amount"])
            except ValueError:
                pass
        
        print(category + ": " + str(total))
        for expense in category_expenses:
            print("  - " + expense["date"] + " | " + expense["description"] + " | " + expense["amount"])


def show_all_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\nAll Expenses:")
    for expense in expenses:
        print(expense["date"] + " | " + expense["category"] + " | " + expense["description"] + " | " + expense["amount"])


def show_menu():
    print("\n" + "=" * 40)
    print(" PERSONAL EXPENSE TRACKER ")
    print("=" * 40)
    print("1. Add Expense")
    print("2. Show Total Expenses")
    print("3. Show Expenses by Category")
    print("4. Show All Expenses")
    print("5. Exit")


def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_total_expenses(expenses)
        elif choice == "3":
            show_expenses_by_category(expenses)
        elif choice == "4":
            show_all_expenses(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()