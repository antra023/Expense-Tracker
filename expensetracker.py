import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ["Food", "Transportation", "Entertainment", "Others"]
        
    def add_expense(self, amount, description, category):
        if category not in self.categories:
            category = "Others"
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        
    def save_data(self, filename="expenses.json"):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)
            
    def load_data(self, filename="expenses.json"):
        try:
            with open(filename, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []
            
    def monthly_summary(self):
        summary = {}
        for expense in self.expenses:
            month = expense["date"][:7]
            if month not in summary:
                summary[month] = 0
            summary[month] += expense["amount"]
        return summary
    
    def category_summary(self):
        summary = {category: 0 for category in self.categories}
        for expense in self.expenses:
            summary[expense["category"]] += expense["amount"]
        return summary
    
    def display_expenses(self):
        for expense in self.expenses:
            print(f"{expense['date']}: {expense['description']} - ${expense['amount']} ({expense['category']})")

# User Interface Example
def main():
    tracker = ExpenseTracker()
    tracker.load_data()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            category = input("Enter category: ")
            tracker.add_expense(amount, description, category)
        elif choice == "2":
            tracker.display_expenses()
        elif choice == "3":
            print(tracker.monthly_summary())
        elif choice == "4":
            print(tracker.category_summary())
        elif choice == "5":
            tracker.save_data()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
