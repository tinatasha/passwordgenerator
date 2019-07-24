import unittest
from password import User

class TestUser(unittest.TestCase):
    """
    Class for testing the behaviour of the user class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_user = User("Tina","Tasha","blackfaffp1")
		
		def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_user.first_name,"Tina")
        self.assertEqual(self.new_user.last_name,"Tasha")
        self.assertEqual(self.new_user.password,"blackfaffp1")
		
		def test_save_user(self):
        """
        Test to check whether app saves user loginn details
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
