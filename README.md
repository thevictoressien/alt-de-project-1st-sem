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

