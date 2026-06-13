# 💰 Expense Tracker

A command-line expense tracking application built with Python. Track your spending, categorize expenses, and analyze your financial habits.

![Python](https://img.shields.io/badge/Python-3.x-blue)

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Data Storage](#data-storage)
- [Example Output](#example-output)
- [Code Structure](#code-structure)
- [Contributing](#contributing)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Add Expenses** | Record expenses with amount, category, and description |
| **Category System** | 8 predefined categories (Food, Transport, Housing, etc.) |
| **Expense History** | View all recorded expenses with dates |
| **Statistics** | Total, average, max, min expenses |
| **Category Breakdown** | Visual percentage breakdown by category |
| **Delete Expenses** | Remove specific expenses |
| **Clear All** | Reset all data |
| **JSON Persistence** | Data saved automatically to `expenses.json` |

---

## 🚀 Installation

### Prerequisites

- Python 3+ installed
- No external dependencies required (uses only standard library)

### Setup

```bash
# Clone or navigate to the project
cd DecodeLabs-Internship_task2

# Run the application
python3 main.py
```

---

## 🎮 Usage

1. Launch the application:
   ```bash
   python3 main.py
   ```

2. Select an option from the main menu (1-6)

3. Follow the on-screen prompts

---

## 📖 Menu Options

### 1. Add Expense
- Enter the amount (positive number)
- Choose a category (1-8)
- Add an optional description
- Expense is saved automatically

### 2. View History
- Displays all expenses in a table format
- Shows: #, Date, Category, Amount, Description
- Includes total at the bottom

### 3. View Statistics
- **General Summary:**
  - Number of expenses
  - Total spent
  - Average expense
  - Maximum expense
  - Minimum expense
- **By Category:**
  - Amount per category
  - Percentage breakdown
  - Visual bar chart

### 4. Delete Expense
- View history first
- Enter the expense number to delete
- Confirmation not required (be careful!)

### 5. Clear All Expenses
- Prompts for confirmation (y/N)
- Deletes all expenses permanently

### 6. Quit
- Exits the application
- Data is automatically saved

---

## 💾 Data Storage

Expenses are stored in a JSON file named `expenses.json` in the same directory.

**Data Format:**
```json
[
  {
    "amount": 50.0,
    "category": "Food",
    "description": "Groceries",
    "date": "2026-06-13 14:30"
  }
]
```

The file is automatically created when you add your first expense.

---

## 📊 Example Output

### Main Menu
```
==================================================
💰 EXPENSE TRACKER - Main Menu
==================================================
  1. Add expense
  2. View history
  3. View statistics
  4. Delete expense
  5. Clear all expenses
  6. Quit
==================================================

> Your choice: 1
```

### Add Expense
```
==================================================
➕ ADD EXPENSE
==================================================

📂 Available categories:
  1. Food
  2. Transport
  3. Housing
  4. Entertainment
  5. Shopping
  6. Health
  7. Phone
  8. Other

> Amount: 50
> Category (1-8): 1
> Description (optional): Groceries

✅ Expense added: 50.0€ - Food
   📝 Groceries
```

### Statistics
```
==================================================
📊 STATISTICS
==================================================

📈 General Summary:
   • Number of expenses: 5
   • Total spent       : 250.00€
   • Average          : 50.00€
   • Max expense      : 100.00€ (Rent)
   • Min expense      : 10.00€ (Coffee)

📊 By category:
   Food             :   100.00€ (40.0%) ████████
   Housing         :   100.00€ (40.0%) ████████
   Transport       :    50.00€ (20.0%) ████
```

---

## 🏗️ Code Structure

```
week2/
├── index.py          # Main application
├── expenses.json    # Data file (auto-generated)
└── README.md        # This file
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `load_expenses()` | Load data from JSON file |
| `save_expenses()` | Save data to JSON file |
| `show_categories()` | Display available categories |
| `add_expense()` | Add new expense with validation |
| `show_history()` | Display expense list |
| `show_statistics()` | Calculate and display stats |
| `delete_expense()` | Remove specific expense |
| `clear_all()` | Delete all expenses |
| `main_menu()` | Main application loop |

### Key Concepts Demonstrated

- **Math Operations**: Accumulator pattern (`total += amount`)
- **Data Structures**: Lists, dictionaries
- **File I/O**: JSON read/write
- **Error Handling**: Try/except for invalid input
- **User Input**: Input validation and loops

---


---

DecodeLabs Internship