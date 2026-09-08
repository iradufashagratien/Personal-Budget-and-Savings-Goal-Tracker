# Project Requirements

## 1. Problem Statement

Managing personal finances can be difficult when income, expenses, and savings are not properly tracked.

People may spend money without knowing how much they are spending in different categories, making it difficult to identify unnecessary expenses or reach savings targets.

The purpose of this project is to develop a simple command-line application that helps users record their financial transactions, manage savings goals, and understand their overall financial situation.

## 2. Functional Requirements

The system should allow users to:

### Transaction Management

* Add income and expense transactions.
* View recorded transactions.
* Update existing transactions.
* Delete transactions.
* Search or filter transactions.
* Validate transaction information.

### Savings Goals

* Create a savings goal.
* View existing savings goals.
* Update a savings goal.
* Delete a savings goal.
* Add money towards a savings goal.
* Track progress towards a savings target.
* Identify completed and incomplete savings goals.

### Analysis and Reports

The system should provide at least two analysis features, including:

* Total income.
* Total expenses.
* Current balance.
* Spending by category.
* Highest spending category.
* Financial or monthly summaries.

### Menu and Error Handling

* Provide a numbered main menu.
* Allow users to repeatedly select options until they choose to exit.
* Handle invalid menu choices without crashing.
* Validate user input.
* Handle invalid numbers and amounts.
* Handle empty data appropriately.

## 3. Data Requirements

The application should store financial information using appropriate Python data structures such as lists and dictionaries.

### Transaction Data

Each transaction should contain relevant information such as:

* ID
* Type (income or expense)
* Amount
* Category
* Description/date where applicable

### Savings Goal Data

Each savings goal should contain:

* ID
* Goal name
* Target amount
* Amount saved

### Data Persistence

The application should use a JSON or CSV file to store data so that information can be saved and loaded between program sessions.

The system should also handle cases where:

* The data file does not exist.
* The data file is empty or unreadable.
* The stored data is invalid.

## 4. GCGO Connection

The project supports responsible financial behaviour by helping users understand and manage their spending.

The application encourages users to:

* Track where their money is going.
* Identify spending patterns.
* Avoid unnecessary spending.
* Set savings targets.
* Monitor progress towards financial goals.

This connects the project to responsible consumption and financial wellbeing.

## 5. Scope of the Project

The project is a small Python command-line application designed for basic personal budgeting and savings tracking.

### Included in the scope:

* Income and expense tracking.
* Savings goal management.
* Basic financial analysis.
* Search and filtering.
* Data storage using JSON or CSV.
* Input validation and error handling.
* A menu-driven command-line interface.

### Outside the scope:

* Online banking integration.
* Real-time bank account information.
* Online payments or money transfers.
* Investment management.
* Multiple user accounts.
* A graphical or mobile user interface.

The project focuses on demonstrating programming, data structures, modular programming, file handling, validation, and basic data analysis using Python's standard library.
