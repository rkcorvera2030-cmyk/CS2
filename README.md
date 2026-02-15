## Quarter 3 Updated Project Documentation (Progress Update)

## Project Title

CodeQuest: School Expense Tracker

## Updated Problem Statement

Many students struggle to manage their daily spending and often do not record where their money goes. Without a simple tracking tool, budgeting becomes difficult. This project provides a beginner-friendly expense tracker program that records, saves, and summarizes expenses to help students build better spending habits.

## Updated Project Objectives

1. Let students add, edit, and delete expense records.
2. Automatically save and load expense data using a JSON file.
3. Calculate totals, monthly reports, and category summaries.
4. Support budget limits with warning messages.
5. Keep the interface simple through a text-based menu.

## Updated Feature List (Current Version)

* Add, edit, and delete expense entries
* View all expenses with total spending
* Search expenses by date or category
* Monthly spending report
* Category spending summary
* Weekly and monthly budget checking with warnings
* CSV export (expenses.csv)
* Text backup file
* Auto load/save using expenses.json
* Looping menu interface

## Revised File and Function Structure

Main script sections:

* Data persistence: load_data(), save_data() using JSON
* Core features: add_expense(), view_expenses(), search_expenses(), edit_expense(), delete_expense()
* Reports: monthly_report(), category_summary()
* Budget tools: set_budget(), check_budget()
* Export tools: export_csv(), backup()
* Menu controller: menu()

Functions are grouped by purpose to keep the code readable and easy to maintain.

## Technologies and Tools Used

* Python — chosen for simplicity and beginner-friendly syntax
* Built-in libraries: json, csv, datetime — used for file storage, export, and date-based reports
* GitHub — used for version control and progress tracking

## Methodology and Implementation

Expenses are stored in a list where each record contains amount, date, category, and notes. Data is saved locally in a JSON file so records are not lost after closing the program. Each major feature is implemented as a separate function and called through a looping text menu. Since this is a console app, there is no backend–frontend separation.

## Key Design Decisions and Trade-offs

* Used a text-based interface instead of a graphical UI to reduce complexity
* Used JSON and CSV instead of a database for easier setup
* Focused on readability over advanced optimization for student understanding

## Planned Inputs and Outputs (Current)

Inputs:

* Expense amount
* Date (YYYY-MM-DD)
* Category
* Notes
* Budget limits

Outputs:

* Expense list display
* Total spending
* Monthly and category summaries
* Budget warning messages
* CSV and backup files

## GitHub Repository Notes

* Organized file structure with grouped functions
* Descriptive commit messages for each feature update
* README includes setup steps, features, and progress status
* Branches may be used for feature testing

## Programming and Computing Ethics

This project follows basic computing ethics:

* Respect for intellectual property and open-source rules
* APA-style credit for references when used
* Simple and readable interface for accessibility
* User privacy protected since all data is stored locally
* Guided by principles from the ACM Code of Ethics

## Group Members

* Cathleah Pabia
* Rhyz Kym Corvera
* Meil Antepasado
