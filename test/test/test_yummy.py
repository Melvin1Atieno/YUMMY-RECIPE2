import unittest
from app/app.py import YummyAccountRegistration
class YummyAccountRegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.myrecipeaccount = YummyAccountRegistration()
    def test_get_firstname(self,firstnmae):
        self.firstname = "melvin"
        self.assertNotIn(self.irstname, self.invalid, msg ="get_firstname invalid characters")
        self.assertNotEqual(self.firstname, " " , msg="get_firstname passes empty")
    def test_get_lastname(self,lastname):
        self.lastname = "atieno"
        self.assertNotIn(self.lastname, self.invalid, msg = "get_lastname passes invalid characters")
        self.asserNotEqual(self.lastname, self.invalid, msg="get_last name passes empty")
    def test_get_username(self,username):
        self.username = melvinatien0
        self.assertNotIn(self.username, self.invalid, msg = "get_username passes invalid characters")
        self.asserNotEqual(self.username, self.invalid, msg="get_username name passes empty")
    def test_get_email(self,email):
        self.email = "melvinatieno@gmail.com"
        self.assertNotIn(self.email," ", msg = "get_email method passes invalid email")
    def test_get_password(self,password):
        self.pasword = "mypassword"
        self.assertTrue(len(self.password) >= 8, msg = "get_password passes short passwords")
    #def test_sub_class(self):
        #self.assertTrue(issubclass(YummyAccountLogin, YummyAccountRegistration, msg="YummyAccountlogin class not subclass"))
