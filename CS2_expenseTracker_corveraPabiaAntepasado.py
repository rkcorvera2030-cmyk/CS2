# CS2 Video Presentation | Pabia, Corvera, Antepasado
# Hi Sir!

import csv

expenses = []
monthly_budget = None
weekly_budget = None


def add_expense():
    amt = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    cat = input("Category: ")
    note = input("Notes: ")

    expenses.append([amt, date, cat, note])
    print("Added!")


def view_expenses():
    total = 0
    for e in expenses:
        print(e)
        total += e[0]
    print("Total:", total)


def search_expenses():
    key = input("Search (date or category): ")
    for e in expenses:
        if key in e[1] or key in e[2]:
            print(e)


def show_list():
    for i, e in enumerate(expenses):
        print(i, e)


def edit_expense():
    show_list()
    i = int(input("Pick number to edit: "))

    if i < 0 or i >= len(expenses):
        print("Invalid.")
        return

    expenses[i][0] = float(input("New amount: "))
    expenses[i][1] = input("New date: ")
    expenses[i][2] = input("New category: ")
    expenses[i][3] = input("New notes: ")
    print("Updated!")


def delete_expense():
    show_list()
    i = int(input("Pick number to delete: "))

    if 0 <= i < len(expenses):
        expenses.pop(i)
        print("Deleted!")
    else:
        print("Invalid.")


def monthly_report():
    month = input("Month (YYYY-MM): ")
    total = sum(e[0] for e in expenses if e[1].startswith(month))
    print("Total this month:", total)


def set_budget():
    global monthly_budget, weekly_budget
    monthly_budget = float(input("Monthly budget: "))
    weekly_budget = float(input("Weekly budget: "))
    print("Budgets set!")


def check_budget():
    if monthly_budget is None:
        return
    total = sum(e[0] for e in expenses)
    if total > monthly_budget:
        print("WARNING: Over monthly budget!")


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


def menu():
    while True:
        print("\n1 Add")
        print("2 View")
        print("3 Search")
        print("4 Edit")
        print("5 Delete")
        print("6 Monthly Report")
        print("7 Set Budget")
        print("8 Export CSV")
        print("9 Backup")
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
            set_budget()
        elif choice == "8":
            export_csv()
        elif choice == "9":
            backup()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        check_budget()


menu()
