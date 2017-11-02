import unittest
from YUMMY.views import app


class FlaskTestCase(unittest.TestCase):


    def test_index_page_loads(self):
        '''tests whether the index page loads'''
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)
    
    def test_registration_loads(self):
        '''tests whether registration page loads'''
        tester = app.test_client(self)
        response = tester.get("/user_registration", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        '''tests whether the login page loads, brings status code 200'''
        tester = app.test_client(self)
        response = tester.get("/login", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_homepage_loads(self):
        '''tests whether the homepage loads '''
        tester = app.test_client(self)
        response = tester.get("/homepage", content_type="html/text")
        self.assertEqual(response.status_code, 200)
      

    


if __name__ == "__main__":
    unittest.main()
