#Pabia, Corvera, Antepasado: Video presentation

import csv
import json
from datetime import datetime

expenses = []
monthly_budget = None
weekly_budget = None

DATA_FILE = "expenses.json"


# -----------------------------
# DATA PERSISTENCE
# -----------------------------

def load_data():
    global expenses
    try:
        with open(DATA_FILE, "r") as f:
            expenses = json.load(f)
    except:
        expenses = []


def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f)


# -----------------------------
# CORE FUNCTIONS
# -----------------------------

def add_expense():
    try:
        amt = float(input("Amount: "))
    except:
        print("Invalid amount.")
        return

    date = input("Date (YYYY-MM-DD): ")
    cat = input("Category: ")
    note = input("Notes: ")

    expenses.append([amt, date, cat, note])
    save_data()
    print("Added!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0
    print("\n--- Expense List ---")
    for i, e in enumerate(expenses):
        print(f"{i}. Amount: {e[0]} | Date: {e[1]} | Category: {e[2]} | Note: {e[3]}")
        total += e[0]

    print("Total:", total)


def search_expenses():
    key = input("Search (date or category): ")
    found = False

    for e in expenses:
        if key.lower() in e[1].lower() or key.lower() in e[2].lower():
            print(e)
            found = True

    if not found:
        print("No matching expenses found.")


def show_list():
    for i, e in enumerate(expenses):
        print(i, e)


def edit_expense():
    show_list()
    try:
        i = int(input("Pick number to edit: "))
    except:
        print("Invalid input.")
        return

    if i < 0 or i >= len(expenses):
        print("Invalid index.")
        return

    try:
        expenses[i][0] = float(input("New amount: "))
    except:
        print("Invalid amount.")
        return

    expenses[i][1] = input("New date: ")
    expenses[i][2] = input("New category: ")
    expenses[i][3] = input("New notes: ")

    save_data()
    print("Updated!")


def delete_expense():
    show_list()
    try:
        i = int(input("Pick number to delete: "))
    except:
        print("Invalid input.")
        return

    if 0 <= i < len(expenses):
        expenses.pop(i)
        save_data()
        print("Deleted!")
    else:
        print("Invalid index.")


def monthly_report():
    month = input("Month (YYYY-MM): ")
    total = sum(e[0] for e in expenses if e[1].startswith(month))
    print("Total this month:", total)


def category_summary():
    summary = {}
    for e in expenses:
        cat = e[2]
        summary[cat] = summary.get(cat, 0) + e[0]

    print("\n--- Category Summary ---")
    for cat, total in summary.items():
        print(cat, ":", total)


# -----------------------------
# BUDGET FUNCTIONS
# -----------------------------

def set_budget():
    global monthly_budget, weekly_budget

    try:
        monthly_budget = float(input("Monthly budget: "))
        weekly_budget = float(input("Weekly budget: "))
    except:
        print("Invalid budget input.")
        return

    print("Budgets set!")


def check_budget():
    if monthly_budget is None:
        return

    total = sum(e[0] for e in expenses)

    if total > monthly_budget:
        print("WARNING: Over monthly budget!")

    # Weekly check
    if weekly_budget is not None:
        current_week = datetime.now().strftime("%Y-%W")
        weekly_total = sum(
            e[0] for e in expenses
            if datetime.strptime(e[1], "%Y-%m-%d").strftime("%Y-%W") == current_week
        )

        if weekly_total > weekly_budget:
            print("WARNING: Over weekly budget!")


# -----------------------------
# EXPORT & BACKUP
# -----------------------------

def export_csv():
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Date", "Category", "Notes"])
        writer.writerows(expenses)
    print("CSV exported!")


def backup():
    with open("backup.txt", "w") as f:
        for e in expenses:
            f.write(str(e) + "\n")
    print("Backup saved!")


# -----------------------------
# MENU SYSTEM
# -----------------------------

def menu():
    load_data()

    while True:
        print("\n1 Add")
        print("2 View")
        print("3 Search")
        print("4 Edit")
        print("5 Delete")
        print("6 Monthly Report")
        print("7 Category Summary")
        print("8 Set Budget")
        print("9 Export CSV")
        print("10 Backup")
        print("0 Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            edit_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            monthly_report()
        elif choice == "7":
            category_summary()
        elif choice == "8":
            set_budget()
        elif choice == "9":
            export_csv()
        elif choice == "10":
            backup()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        check_budget()


menu()
