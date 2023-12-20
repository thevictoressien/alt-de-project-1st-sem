import unittest
from tests import TestExpense, TestExpenseDatabase
import tests

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(tests)
runner = unittest.TextTestRunner()
runner.run(suite)