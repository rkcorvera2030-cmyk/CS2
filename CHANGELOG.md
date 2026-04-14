# CHANGELOG

All notable changes to this project will be documented in this file.  
The format follows *Semantic Versioning*: vMAJOR.MINOR.PATCH  

* *MAJOR*: Significant changes or new modules  
* *MINOR*: New features or improvements  
* *PATCH*: Small fixes or adjustments  

---

## [v1.0.0]

* Initial project proposal completed.  
* Added project objectives, planned features, and logic plan.  

## [v1.1.0]

* Created basic Python program structure.  
* Implemented looping text-based main menu.  

## [v1.2.0]

* Added **Add Expense** feature with amount, date, category, and notes input.  
* Stored expenses in a list structure.  

## [v1.3.0]

* Implemented **View Expenses** feature.  
* Added automatic total expense calculation.  

## [v1.4.0]

* Added **Search Expenses** by date or category.  
* Improved menu navigation and prompts.  

## [v1.5.0]

* Added **Edit Expense** feature.  
* Added **Delete Expense** feature.  
* Added input validation for amount values.  

## [v1.6.0]

* Implemented **Monthly Spending Report** feature.  
* Added **Category Summary** totals.  

## [v1.7.0]

* Added **JSON data persistence** (expenses.json).  
* Program now auto-loads data at startup and saves after every change.  

## [v1.8.0]

* Added **CSV export** feature (expenses.csv).  
* Added **text backup** file feature.  
* Organized functions into clear code sections.  

## [v1.9.0]

* Added **weekly and monthly budget setting**.  
* Implemented automatic **budget warning alerts** when limits are exceeded.  
* Improved error handling for invalid inputs.  

## [v2.0.0]

* Refactored function grouping and documentation to match repository standards.  
* Updated README and methodology sections.  
* Improved code comments and repository organization for Quarter 3 submission.  

---

## [v2.1.0]

* Migrated project from **Python (text-based)** to **Web Application (HTML, CSS, JavaScript)**.  
* Implemented structured UI with input fields, dropdowns, and tables.  
* Replaced file-based storage with **localStorage** for persistent browser data.  

## [v2.2.0]

* Added **interactive expense table display** using dynamic DOM rendering.  
* Implemented centralized `render()` function to update UI in real time.  
* Added formatted currency display (₱ with two decimal places).  

## [v2.3.0]

* Implemented **budget system** with input and real-time display.  
* Added automatic **budget exceeded warning** using status bar alerts.  
* Linked total expenses with budget comparison logic.  

## [v2.4.0]

* Added **edit mode system** using index tracking (`editIndex`).  
* Combined **Add and Update** functionality into a single button.  
* Improved user workflow for modifying existing entries.  

## [v2.5.0]

* Improved **input validation** for amount and budget fields.  
* Added temporary **error/status notification bar** for user feedback.  
* Prevented invalid or empty data entries.  

## [v2.6.0]

* Enhanced UI with **card layout design**, shadows, and rounded components.  
* Added styled buttons for **edit (orange)** and **delete (red)** actions.  
* Improved table formatting and readability.  

## [v2.7.0]

* Optimized data handling and UI refresh flow.  
* Ensured all actions (add, edit, delete, budget set) trigger `render()`.  
* Finalized system for consistent behavior and stable performance.  
