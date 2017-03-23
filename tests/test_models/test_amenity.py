import unittest
from datetime import datetime
from models import *
from console import HBNBCommand


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = Amenity()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")
        self.cli.do_destroy("Amenity " + self.model.id)

if __name__ == "__main__":
    unittest.main()
