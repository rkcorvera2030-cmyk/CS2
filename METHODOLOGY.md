# Methodology and Technical Documentation

## CodeQuest: School Expense Tracker

## Overview

This project is a Python-based expense tracker that helps students record and manage their daily spending. The program runs in a text-based menu and allows users to add, view, search, edit, and delete expenses. It also supports reports, budgets, and data export. The system is designed to be simple, readable, and easy to maintain.

---

## How Core Features Were Implemented

Expenses are stored in a list where each record contains four values: amount, date, category, and notes. Each major feature is written as a separate function to keep the code modular.

Core functions include:

* Adding expenses through user input with amount validation
* Viewing all expenses with automatic total calculation
* Searching by date or category using string matching
* Editing and deleting entries using index selection
* Monthly reports using date prefix checking
* Category summaries using a dictionary total per category

A looping menu function controls the program flow and repeatedly asks the user for actions until exit is chosen.

---

## Data Storage Method

The program uses a JSON file named **expenses.json** for data persistence.

* When the program starts, it loads saved data using `load_data()`
* When changes are made, it saves using `save_data()`
* This prevents data loss between runs
* JSON was chosen because it is simple and built into Python

---

## Budget and Date Logic

The program allows users to set weekly and monthly budgets.
Totals are computed using sum calculations on stored expenses.

Weekly budget checking uses the Python datetime library to compare the stored expense dates with the current week number. If totals go over the limit, the program prints a warning message.

---

## Export and Backup Features

Two safety features are included:

* CSV export using the csv library for spreadsheet use
* Text backup file that writes all records line by line

These features help prevent accidental data loss and improve usability.

---

## Technologies Used (with Justification)

**Python** — beginner-friendly and good for list and file operations
**json library** — used for saving and loading structured data
**csv library** — used for spreadsheet-compatible export
**datetime library** — used for weekly and monthly budget checks
**GitHub** — used for version control and collaboration

These tools were selected because they are built-in, reliable, and appropriate for a student-level project.

---

## Backend–Frontend Communication

Not applicable. The project is a console-based application. User input and program processing happen in the same script. There is no separate frontend or backend system.

---

## Key Design Decisions and Trade-offs

* A text-based interface was used instead of a graphical UI to reduce complexity
* JSON file storage was used instead of a database for easier setup
* Functions were separated by feature to improve readability
* Simplicity and clarity were prioritized over advanced optimization

---

## GitHub Repository Practices

The repository is organized with:

* Grouped functions and clear section comments
* Descriptive commit messages for each feature update
* Updated README with setup steps and progress status
* Version tracking through a CHANGELOG file
* Optional branch use for testing features

---

## Programming and Computing Ethics

This project follows basic programming and computing ethics:

* Intellectual property is respected
* No restricted or paid code was copied
* Learning sources are credited in APA style when used
* The interface is simple and readable for accessibility
* User privacy is protected because all data is stored locally
* Ethical guidance is based on general ACM Code of Ethics principles

## References

Python Software Foundation. (2024). *Python documentation*. [https://docs.python.org/3/](https://docs.python.org/3/)

Python Software Foundation. (2024). *json — JSON encoder and decoder*. [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)

Python Software Foundation. (2024). *csv — CSV file reading and writing*. [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)

Python Software Foundation. (2024). *datetime — Basic date and time types*. [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

Association for Computing Machinery. (2018). *ACM code of ethics and professional conduct*. [https://www.acm.org/code-of-ethics](https://www.acm.org/code-of-ethics)
