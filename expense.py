"""
expense.py defines two classes for managing expense data - Expense and ExpenseDatabase.

Expense represents a single expense record with id, title, amount and timestamp attributes.
The Expense class provides methods to update the expense data and convert to a dict.

ExpenseDatabase stores a list of Expense objects and provides methods to add, remove, 
retrieve expenses by id or title, and convert the entire database to a dict.

These classes allow for creating, storing, updating, retrieving and serializing expense data.
"""
from uuid import uuid4
from datetime import datetime
import pytz


class Expense:

    """Represents an expense record."""

    def __init__(self, title: str, amount: float) -> None:
        
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        
        self.title = title
        self.amount = amount
        self.id = str(uuid4())
        self.created_at = datetime.utcnow().replace(tzinfo=pytz.utc)\
            .astimezone(pytz.timezone('Europe/Paris')).isoformat()
        self.updated_at = datetime.utcnow().replace(tzinfo=pytz.utc)\
            .astimezone(pytz.timezone('Europe/Paris')).isoformat()


    def update(self, title: str = None, amount: float = None) -> None:

        """Updates the expense title and amount.

        Parameters:
        - title (str, optional): The new title for the expense.
        - amount (float, optional): The new amount for the expense.
        """
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow().replace(tzinfo=pytz.utc)\
            .astimezone(pytz.timezone('Europe/Paris'))


    def to_dict(self) -> dict:

        """Converts Expense object to dictionary."""

        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    
    def __repr__(self) -> str:
      return f"Expense(id={self.id}, title={self.title}, amount={self.amount}, " \
               f"created_at={self.created_at}, updated_at={self.updated_at})"



class ExpenseDatabase:

    """Stores expenses and allows adding, removing, and retrieving records.

    Attributes:
    - expenses (list): A list containing Expense objects.
    """

    def __init__(self):
        self.expenses = list()


    def add_expense(self, *expenses: Expense) -> None:
        """Adds new expense records."""
        for expense in expenses:
            self.expenses.append(expense)


    def remove_expense(self, id: str) -> Expense:
        """Removes expense with given ID.""" 
        self.expenses = [expense for expense in self.expenses if expense.id != id]


    def get_expense_by_id(self, id: str) -> Expense:
        """Retrieves expense with given ID."""
        return next((expense for expense in self.expenses if expense.id == id), None)


    def get_expenses_by_title(self, title: str) -> list[Expense]:
        """Retrieves expenses matching given title."""
        return [expense for expense in self.expenses if expense.title == title]


    def to_dict(self) -> list[dict]:
        """Converts expenses to list of dict."""
        return [expense.to_dict() for expense in self.expenses]
    

    def __repr__(self) -> str:
        return f"ExpenseDatabase(expenses={self.expenses})"
