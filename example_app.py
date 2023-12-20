import pandas as pd
from expense import Expense, ExpenseDatabase

print("Welcome to the expense management system!") 

database = ExpenseDatabase()

# Add some initial sample expenses
expense1 = Expense("Groceries", 25.50)
expense2 = Expense("Gas", 40.00)
expense3 = Expense("Dinner", 55.25)

database.add_expense(expense1, expense2, expense3)

while True:
    print("\nWhat would you like to do?")
    print("1. Add new expense")
    print("2. Update expense")
    print("3. Remove expense") 
    print("4. View expenses")
    print("5. Get expense by ID")
    print("6. Get expenses by title")
    print("7. Export expenses")
    print("8. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter title: ")
        amount = float(input("Enter amount: "))
        expense = Expense(title, amount)
        database.add_expense(expense)
        print("Expense added!")

    elif choice == '2':
        id = input("Enter ID of expense to update: ")
        expense = database.get_expense_by_id(id)
        if expense:
            title = input("Enter new title (or leave blank): ")
            amount = input("Enter new amount (or leave blank): ")
            if title:
                expense.title = title
            if amount: 
                expense.amount = float(amount)
            expense.update()
            print("Expense updated!")
        else:
            print("Invalid ID - could not find expense.")
            
    elif choice == '3':
        id = input("Enter ID of expense to remove: ")
        database.remove_expense(id)
        print("Expense removed!")
        
    elif choice == '4':
        expenses = database.to_dict()
        df = pd.DataFrame(expenses)
        print(df)
        
    elif choice == '5':
        id = input("Enter ID to search for: ")
        expense = database.get_expense_by_id(id)
        if expense:
            print(expense.to_dict())
        else:
            print("No expense with that ID found.")
            
    elif choice == '6':
        title = input("Enter title to search for: ")
        expenses = database.get_expenses_by_title(title)
        print(expenses)
        
    elif choice == '7':
        expenses = database.to_dict()
        print(expenses)
        
    elif choice == '8':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice - please enter a number between 1 and 8")
