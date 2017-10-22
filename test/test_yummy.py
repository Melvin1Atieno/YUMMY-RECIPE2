import unittest
from app.py import YummyAccountRegistration
class YummyAccountRegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.myrecipeaccount = YummyAccountRegistration()
    def test_get_firstname(self):
        self.assertNotIn(self.firstname, self.invalid, msg ="get_firstname invalid characters")
        self.assertNotEqual(self.firstname, " " , msg="get_firstname passes empty")
    def test_get_lastname(self):
        self.assertNotIn(self.lastname, self.invalid, msg = "get_lastname passes invalid characters")
        self.asserNotEqual(self.lastname, self.invalid, msg="get_last name passes empty")
    def test_get_email(self):
        self.assertNotIn(self.email," ", msg = "get_email method passes invalid email")
    def test_get_password(self):
        self.assertTrue(len(self.password) >= 8, msg = "get_password passes short passwords")
    def test_confirm_password(self):
        self.assertEqual(self.password, self.reenteredpassword, msg="confirm method invalid")
    def test_sub_class(self):
        self.assertTrue(issubclass(YummyAccountLogin, YummyAccountRegistration, msg="YummyAccountlogin class not subclass"))