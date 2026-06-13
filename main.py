#!/usr/bin/env python3
"""
Expense Tracker - Expense Management Tool
Features:
- Add expenses with category
- View expense history
- Calculate average, max, min
- Statistics by category
- Save to JSON file
"""

import json
import os
from datetime import datetime

# Data file for persistence
DATA_FILE = "expenses.json"

# Available categories
CATEGORIES = {
    "1": "Food",
    "2": "Transport",
    "3": "Housing",
    "4": "Entertainment",
    "5": "Shopping",
    "6": "Health",
    "7": "Phone",
    "8": "Other"
}

# List to store expenses
expenses = []


def load_expenses():
    """Load expenses from file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses():
    """Save expenses to file"""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)


def show_categories():
    """Show available categories"""
    print("\n📂 Available categories:")
    for key, value in CATEGORIES.items():
        print(f"  {key}. {value}")


def add_expense():
    """Add a new expense"""
    print("\n" + "="*50)
    print("➕ ADD EXPENSE")
    print("="*50)
    
    # Ask for amount
    while True:
        try:
            amount = float(input("\n> Amount: "))
            if amount <= 0:
                print("❌ Amount must be positive")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number")
    
    # Ask for category
    show_categories()
    while True:
        category_choice = input("\n> Category (1-8): ")
        if category_choice in CATEGORIES:
            category = CATEGORIES[category_choice]
            break
        print("❌ Invalid choice")
    
    # Ask for description
    description = input("> Description (optional): ").strip()
    if not description:
        description = "No description"
    
    # Save expense
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)
    save_expenses()
    
    print(f"\n✅ Expense added: {amount}€ - {category}")
    print(f"   📝 {description}")


def show_history():
    """Show expense history"""
    print("\n" + "="*50)
    print("📜 EXPENSE HISTORY")
    print("="*50)
    
    if not expenses:
        print("\n❌ No expenses recorded")
        return
    
    total = 0
    print(f"\n{'#':<4} {'Date':<18} {'Category':<20} {'Amount':<10} {'Description'}")
    print("-" * 70)
    
    for i, exp in enumerate(expenses, 1):
        total += exp["amount"]
        print(f"{i:<4} {exp['date']:<18} {exp['category']:<20} {exp['amount']:<10.2f} {exp['description']}")
    
    print("-" * 70)
    print(f"{'TOTAL':<44} {total:.2f}€")


def show_statistics():
    """Show statistics"""
    print("\n" + "="*50)
    print("📊 STATISTICS")
    print("="*50)
    
    if not expenses:
        print("\n❌ No expenses recorded")
        return
    
    # Basic calculations
    total = sum(exp["amount"] for exp in expenses)
    average = total / len(expenses)
    max_expense = max(expenses, key=lambda x: x["amount"])
    min_expense = min(expenses, key=lambda x: x["amount"])
    
    print(f"\n📈 General Summary:")
    print(f"   • Number of expenses: {len(expenses)}")
    print(f"   • Total spent       : {total:.2f}€")
    print(f"   • Average          : {average:.2f}€")
    print(f"   • Max expense      : {max_expense['amount']:.2f}€ ({max_expense['description']})")
    print(f"   • Min expense      : {min_expense['amount']:.2f}€ ({min_expense['description']})")
    
    # Statistics by category
    print(f"\n📊 By category:")
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]
    
    # Sort by amount
    sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    
    for cat, amount in sorted_cats:
        percentage = (amount / total) * 100
        bar = "█" * int(percentage / 5)
        print(f"   {cat:<20} : {amount:>8.2f}€ ({percentage:>5.1f}%) {bar}")


def delete_expense():
    """Delete an expense"""
    if not expenses:
        print("\n❌ No expenses to delete")
        return
    
    show_history()
    
    while True:
        try:
            choice = int(input("\n> Expense number to delete: "))
            if 1 <= choice <= len(expenses):
                removed = expenses.pop(choice - 1)
                save_expenses()
                print(f"\n✅ Expense deleted: {removed['amount']}€ - {removed['description']}")
                break
            print("❌ Invalid number")
        except ValueError:
            print("❌ Please enter a number")


def clear_all():
    """Clear all expenses"""
    if not expenses:
        print("\n❌ No expenses to clear")
        return
    
    confirm = input("> Confirm (y/N)? ")
    if confirm.lower() == 'y':
        expenses.clear()
        save_expenses()
        print("\n✅ All expenses have been cleared")


def main_menu():
    """Main menu"""
    global expenses
    expenses = load_expenses()
    
    while True:
        print("\n" + "="*50)
        print("💰 EXPENSE TRACKER - Main Menu")
        print("="*50)
        print("  1. Add expense")
        print("  2. View history")
        print("  3. View statistics")
        print("  4. Delete expense")
        print("  5. Clear all expenses")
        print("  6. Quit")
        print("="*50)
        
        choice = input("\n> Your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_history()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            clear_all()
        elif choice == "6":
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice")


if __name__ == "__main__":
    main_menu()