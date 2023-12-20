# Expense Management System

This project implements two classes, `Expense` and `ExpenseDatabase`, to model and manage financial expenses.

## Expense Class

Represents an individual financial expense.

### Attributes

1. **id**: A unique identifier generated as a UUID string.
2. **title**: A string representing the title of the expense.
3. **amount**: A float representing the amount of the expense.
4. **created_at**: A timestamp indicating when the expense was created (UTC).
5. **updated_at**: A timestamp indicating the last time the expense was updated (UTC).

### Methods

1. **__init__**: Initializes the attributes.
2. **update**: Allows updating the title and/or amount, updating the updated_at timestamp.
3. **to_dict**: Returns a dictionary representation of the expense.

## ExpenseDatabase Class

Manages a collection of Expense objects.

### Attributes

1. **expenses**: A list storing Expense instances.

### Methods

1. **__init__**: Initializes the list.
2. **add_expense**: Adds an expense.
3. **remove_expense**: Removes an expense.
4. **get_expense_by_id**: Retrieves an expense by ID.
5. **get_expenses_by_title**: Retrieves expenses by title (returning a list).
6. **to_dict**: Returns a list of dictionaries representing expenses.

## Instructions

### Cloning and Forking the Project

```bash
# Fork the repository and clone your fork
git clone https://github.com/thevictoressien/alt-de-project-1st-sem.git
```

## Installing Dependencies
```bash
pip install -r requirements.txt
```
## Python version
```bash
Python 3.11.1
```

## Using the Expense Management System
1. Import the Expense and ExpenseDatabase classes:
``` python
from expense import Expense, ExpenseDatabase
```
2. Create a database instance to store expenses:
```pyhton
database = ExpenseDatabase()
```
Now you can store expenses. 
3. Let's add a sample expense to the database:
```python
expense = Expense("Shoes", 500)
db.add_expense(expense)
Note: Multiple expenses can be added at the same time.
```
4. You can also update the title or amount of an expense:
```python
expense.update("Shoes", 600) # Update amount
```
5. When expenses are in the database, you can retrieve with their unique ID:
```python
db.get_expense_by_id("2135a902-f956-4810-8986-65bdcb3ef08f") 
```
6. You can also remove an unwanted expense using its ID, retrieve all expenses with a prticular title or convert the database to a dictionary for serialization:
```python
# Remove expense
db.remove_expense("2135a902-f956-4810-8986-65bdcb3ef08f")

# Get expenses by title
expenses = db.get_expenses_by_title("Shoes")

# Convert to dictionary
expenses_dict = db.to_dict()
```
See example_app.py for a sample implementation of the Expense and ExpenseDatabase classes.
