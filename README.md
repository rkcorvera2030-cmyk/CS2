#  Quarter 3 Updated Project Documentation (Progress Update)

##  Project Title

**CodeQuest: School Expense Tracker**

---

##  Updated Problem Statement

Many students struggle to manage their daily spending and often do not keep track of where their money goes. Without a simple tool, budgeting becomes difficult and unorganized. This project provides a beginner-friendly **web-based expense tracker** that records, saves, and summarizes expenses to help students develop better spending habits.

---

##  Updated Project Objectives

* Allow users to add, edit, and delete expense records
* Save and load expense data using **localStorage**
* Automatically calculate total expenses
* Support budget limits with warning messages
* Provide a simple and clean user interface

---

##  Updated Feature List (Current Version)

* Add, edit, and delete expense entries
* View all expenses with total spending
* Categorize expenses (Food, Transport, Supplies, Other)
* Budget system with warning notification
* Real-time total calculation
* Auto save/load using browser localStorage
* Simple card-based interface design

---

##  Revised File and Function Structure

###  File Structure

* **index.html** → main structure of the app
* **CSS (inside HTML)** → styling and layout
* **JavaScript (inside HTML)** → logic and functionality

---

###  Function Groups

**Data Handling**

* `localStorage.getItem()` → loads saved data
* `localStorage.setItem()` → saves expenses and budget

**Core Features**

* `addExpense()` → adds or updates expense
* `editExpense()` → loads data into input fields
* `deleteExpense()` → removes selected expense

**Display / UI**

* `render()` → updates table, total, and budget display
* `showError()` → shows warning messages

**Budget System**

* `setBudget()` → saves and updates budget
* budget check inside `render()` → shows warning if exceeded

---

##  Technologies and Tools Used

* **HTML** — used to structure the interface
* **CSS** — used for styling and layout
* **JavaScript** — used for logic and interactivity
* **Browser localStorage** — used for saving data
* **Google Fonts (Inter)** — used for clean typography

---

##  Methodology and Implementation

Expenses are stored in an array where each record contains the amount, category, and note. Data is saved using localStorage so it remains even after refreshing the page. Each feature is handled by a specific JavaScript function. The `render()` function updates the interface dynamically whenever changes are made. Since this is a web app, all processing happens on the client side.

---

##  Key Design Decisions and Trade-offs

* Used a **web interface instead of console** for better user experience
* Used **localStorage instead of a database** for simplicity
* Focused on **clean UI and readability** instead of complex features
* Kept categories fixed using a dropdown to avoid inconsistent input

---

##  Planned Inputs and Outputs (Current)

### Inputs:

* Expense amount
* Category selection
* Notes/description
* Budget value

### Outputs:

* Expense list (table format)
* Total spending
* Budget display
* Warning message if budget is exceeded

---

##  GitHub Repository Notes

* Organized and readable code structure
* Functions grouped by purpose
* README includes features and usage instructions
* Changelog tracks progress updates
* Clear commit messages for each feature added

---

##  Programming and Computing Ethics

This project follows proper computing practices:

* Respects intellectual property and uses proper references
* Includes **APA-style citations** in documentation and presentation
* Provides a simple and accessible interface for users
* Protects user privacy since all data is stored locally
* Guided by principles from the **Association for Computing Machinery Code of Ethics**

---

##  Group Members

* Cathleah Pabia
* Rhyz Kym Corvera
* Meil Antepasado
