import unittest
from expense import Expense, ExpenseDatabase

class TestExpense(unittest.TestCase):

    def test_create_expense(self):
        expense = Expense("Lunch", 10.5)
        self.assertEqual(expense.title, "Lunch")
        self.assertEqual(expense.amount, 10.5)
    
    def test_update_expense(self):
        expense = Expense("Dinner", 15)
        expense.update("Lunch", 10)
        self.assertEqual(expense.title, "Lunch")
        self.assertEqual(expense.amount, 10)

    def test_to_dict(self):
        expense = Expense("Coffee", 5)
        expense_dict = expense.to_dict()
        self.assertEqual(expense_dict['title'], "Coffee")
        self.assertEqual(expense_dict['amount'], 5)
        self.assertIsInstance(expense_dict['id'], str)

class TestExpenseDatabase(unittest.TestCase):

    def setUp(self):
        self.db = ExpenseDatabase()

    def test_add_expense(self):
        expense = Expense("Taxi", 20)
        self.db.add_expense(expense)
        self.assertEqual(len(self.db.expenses), 1)
        self.assertEqual(self.db.expenses[0].title, "Taxi")

    def test_remove_expense(self):
        expense = Expense("Bus", 5)
        self.db.add_expense(expense)
        self.db.remove_expense(expense.id)
        self.assertEqual(len(self.db.expenses), 0)

    def test_get_expense_by_id(self):
        expense = Expense("Train", 15)
        self.db.add_expense(expense)
        fetched = self.db.get_expense_by_id(expense.id)
        self.assertEqual(fetched.title, "Train")

    def test_get_expenses_by_title(self):
        e1 = Expense("Food", 10)
        e2 = Expense("Food", 12)
        self.db.add_expense(e1)
        self.db.add_expense(e2)
        expenses = self.db.get_expenses_by_title("Food")
        self.assertEqual(len(expenses), 2)