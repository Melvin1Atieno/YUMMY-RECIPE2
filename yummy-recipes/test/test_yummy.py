import unittest

# import modules that I will need to use
# Use absolutes imports i.e directoryname.modulename
from ..main.app import YummyRecipeRegistration

class YummyAccountRegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.myrecipeaccount = YummyRecipeRegistration()

    def test_get_firstname(self,firstnmae):
        self.firstname = "melvin"
        self.assertNotIn(self.firstname, self.myrecipeaccount.invalid, msg ="get_firstname invalid characters")
        self.assertNotEqual(self.firstname, " " , msg="get_firstname passes empty")
    def test_get_lastname(self,lastname):
        self.lastname = "atieno"
        self.assertNotIn(self.lastname, self.myrecipeaccount.invalid, msg = "get_lastname passes invalid characters")
        self.assertNotEqual(self.lastname, self.myrecipeaccount.invalid, msg="get_last name passes empty")
    def test_get_username(self,username):
        self.username = "melvinatien0"
        self.assertNotIn(self.username, self.myrecipeaccount.invalid, msg = "get_username passes invalid characters")
        self.assertNotEqual(self.username, self.myrecipeaccount.invalid, msg="get_username name passes empty")
    def test_get_email(self,email):
        self.email = "melvinatieno@gmail.com"
        self.assertNotIn(self.email," ", msg = "get_email method passes invalid email")
    def test_get_password(self,password):
        self.pasword = "mypassword"
        self.assertTrue(len(self.myrecipeaccount.password) >= 8, msg = "get_password passes short passwords")
    #def test_sub_class(self):
        #self.assertTrue(issubclass(YummyAccountLogin, YummyAccountRegistration, msg="YummyAccountlogin class not subclass"))
