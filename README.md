# Expense Management System

## Overview
The aim of this project is to implement two classes, `Expense` and `ExpenseDatabase`, to model and manage financial expenses.

## File Structure
- `expense.py`: Contains implementations of the `Expense` and `ExpenseDatabase` classes.
- `example_app.py`: Contains code that demonstrates how to use the classes implemented in `expense.py`.
- `requirements.txt`: Contains project dependencies.
- `test_runner.py`: Contains code that executes the tests defined in `tests.py`.
- `tests.py`: Contains test cases

## Implementation Description
### Expense Class

Represents an individual financial expense.

#### Attributes

1. **id**: A unique identifier generated as a UUID string.
2. **title**: A string representing the title of the expense.
3. **amount**: A float representing the amount of the expense.
4. **created_at**: A timestamp indicating when the expense was created (UTC).
5. **updated_at**: A timestamp indicating the last time the expense was updated (UTC).

#### Methods

1. **__init__**: Initializes the attributes.
2. **update**: Allows updating the title and/or amount, updating the updated_at timestamp.
3. **to_dict**: Returns a dictionary representation of the expense.
4. **__repr__**: Returns a string representation of the object, providing a detailed view of its attributes.
   
### ExpenseDatabase Class

Manages a collection of Expense objects.

#### Attributes

1. **expenses**: A list storing Expense instances.

#### Methods

1. **__init__**: Initializes the list.
2. **add_expense**: Adds an expense.
3. **remove_expense**: Removes an expense.
4. **get_expense_by_id**: Retrieves an expense by ID.
5. **get_expenses_by_title**: Retrieves expenses by title (returning a list).
6. **to_dict**: Returns a list of dictionaries representing expenses.
7.  **__repr__**: Returns a string representation of the object, providing a detailed view of its attributes.

## Cloning This Project and Installing Dependencies

### Cloning This Project
Clone this repository using the command below in your terminal:
```bash
git clone https://github.com/thevictoressien/alt-de-project-1st-sem.git
```

### Installing Dependencies
The `requirements.txt` file contains the external libraies used in this project. Once the repository has been cloned to a 
local environment proceed to install the dependencies, using:
```bash
pip install -r requirements.txt
```
Note: Have a virtual environment set up already. This can be achieved using the command below:
```bash
python -m venv <virtual_environment_name>
```

### Python version
```bash
Python 3.11.1
```

## Using the Expense Management System
The `example_app.py` file contains a demonstration of how to use the `Expense` and `ExpenseDatabase` classes. 

This file can be run using the command below:
```bash
python example_app.py
```
Note: Run this file from the same directory as the `expense.py` file

OR, just follow the steps below to create an app to explore functionalities of both classes:

1. Create a python file:
```bash
touch new_file.py
```
Note: Run in terminal, in the same directory as `expense.py`

2. Import the Expense and ExpenseDatabase classes:
``` python
from expense import Expense, ExpenseDatabase
```
3. Create a database instance to store expenses:
```pyhton
database = ExpenseDatabase()
```
4. Let's add a sample expense to the database:
```python
expense = Expense("Shoes", 500)
db.add_expense(expense)
# Note: Multiple expenses can be added at the same time.
```
5. You can also update the title or amount of an expense:
```python
expense.update("Shoes", 600) # Update amount
```
6. When expenses are in the database, you can retrieve with their unique ID:
```python
db.get_expense_by_id("2135a902-f956-4810-8986-65bdcb3ef08f") 
```
7. You can also remove an unwanted expense using its ID, retrieve all expenses with a prticular title or convert the database to a dictionary for serialization:
```python
# Remove expense
db.remove_expense("2135a902-f956-4810-8986-65bdcb3ef08f")

# Get expenses by title
expenses = db.get_expenses_by_title("Shoes")

# Convert to dictionary
expenses_dict = db.to_dict()
```
