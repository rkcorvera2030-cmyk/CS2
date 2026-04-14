# Methodology and Technical Documentation

## CodeQuest: School Expense Tracker

---

## Overview

This project is a web-based expense tracker developed using HTML, CSS, and JavaScript. It allows students to record, manage, and monitor their daily expenses through an interactive interface.

The system runs in a browser and provides features such as adding, editing, deleting expenses, setting a budget, and tracking total spending. Data is stored using localStorage, allowing information to persist even after refreshing the page.

The design focuses on simplicity, usability, and real-time updates.

---

## How Core Features Were Implemented

Expenses are stored in a JavaScript array, where each expense contains:

* amount
* category
* note

Each feature is implemented using separate JavaScript functions to keep the code organized and easy to understand.

Core functions include:

* Adding expenses using input fields with validation to prevent invalid values
* Displaying all expenses dynamically using a table
* Editing expenses by loading selected data back into the input fields
* Deleting expenses using array manipulation
* Calculating total expenses automatically during rendering
* Budget checking that displays a warning when exceeded

A central function called `render()` updates the interface every time data changes. This ensures that the displayed data is always accurate.

---

## Data Storage Method

The program uses **localStorage** to store data directly in the browser.

* Expenses are saved as a JSON string under the key `"expenses"`
* Budget is saved under the key `"budget"`
* Data is retrieved using `JSON.parse()` and stored using `JSON.stringify()`

This approach ensures that:

* Data is not lost when the page refreshes
* No external database is required
* The system remains simple and efficient

---

## Budget Logic

The system allows users to set a budget using an input field.

* The total expense is calculated by summing all stored expense amounts
* During rendering, the program compares total expenses with the set budget
* If the total exceeds the budget, a warning message is displayed using the status bar

This provides immediate feedback to the user.

---

## User Interface Design

The interface is divided into sections using card layouts:

* Budget section
* Expense input section
* Expense list and total display

A table is used to display expenses for better organization.

CSS was used to:

* Create a clean and modern layout
* Improve readability using spacing and fonts
* Add hover effects for better user interaction

The design prioritizes clarity and ease of use.

---

## Technologies Used (with Justification)

**HTML** — used to structure the layout and input fields
**CSS** — used to design the interface and improve user experience
**JavaScript** — used to handle logic, data processing, and interactivity
**localStorage API** — used for saving and retrieving data in the browser
**Google Fonts (Inter)** — used for improved typography

These technologies were chosen because they are widely used, beginner-friendly, and suitable for web-based applications.

---

## Backend–Frontend Communication

Not applicable. This project is a client-side web application.

All processing, storage, and display occur within the browser using JavaScript. There is no separate backend server or database.

---

## Key Design Decisions and Trade-offs

* A web-based interface was used instead of a console program to improve usability
* localStorage was used instead of a database to simplify development
* A single-page design was used for faster interaction
* The `render()` function was used to centralize UI updates
* Simplicity and readability were prioritized over advanced features

---

## GitHub Repository Practices

The repository follows good development practices:

* Code is organized into HTML, CSS, and JavaScript sections
* Clear function naming for readability
* Incremental commits showing feature development
* README file explaining the project
* CHANGELOG file tracking updates and improvements

---

## Programming and Computing Ethics

This project follows basic ethical practices:

* No copyrighted or paid code was copied
* Learning resources are properly cited in APA format
* The system is designed to be simple and accessible
* User data is stored locally to protect privacy
* Ethical guidelines are based on general principles of responsible computing

---

## References

Mozilla Developer Network. (2023). *Web storage API*. [https://developer.mozilla.org](https://developer.mozilla.org)

Mozilla Developer Network. (2023). *JavaScript guide*. [https://developer.mozilla.org](https://developer.mozilla.org)

W3Schools. (2023). *HTML, CSS, and JavaScript tutorials*. [https://www.w3schools.com](https://www.w3schools.com)

Google Fonts. (2023). *Inter font*. [https://fonts.google.com](https://fonts.google.com)
