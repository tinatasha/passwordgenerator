import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class to test behaviour of the credentials class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_credentials = Credentials("Github","Kibet1816","@#soccerkibe1816")

    def tearDown(self):
        """
        Method that cleans up after each test
        """
        Credentials.credentials_list = []
