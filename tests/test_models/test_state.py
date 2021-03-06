import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_StateModel(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = State()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")
        self.cli.do_destroy("State " + self.model.id)

if __name__ == "__main__":
    unittest.main()
