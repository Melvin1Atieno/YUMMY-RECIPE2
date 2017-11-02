import unittest
from YUMMY.models import UserAccount, RecipeCategories, Recipe

class TestModels(unittest.TestCase):

    def setUp(self):
        '''initializes an instance of the class UserAccount'''
        self.new_user = UserAccount() 
        
    def test_add_new_method_adds_new_user_email_to_user_list(self):
        '''tests whether user's email is added to list of users emails'''
        self.new_user.add_new("mel", "mel@gmail.com", "123","123")
        self.assertIn("mel@gmail.com", self.new_user.users)

    def test_add_new_method_does_not_add_existing_user(self):
        '''test whether a user gets a message if they already have an account '''
        self.new_user = UserAccount()
        self.new_user.add_new("mel", "mel@gmail.com", "123", "123")
        result = self.new_user.add_new("mel", "mel@gmail.com", "123", "123")
        self.assertEqual(result, "the email is registered to an existing user")

    def test_add_new_method(self):
        '''test whether user can create an account'''
        self.new_user = UserAccount()
        results = self.new_user.add_new("mel", "mel@gmail.com", "123", "123")
        self.assertEqual(results, "ACCOUNT SUCCEFULLY CREATED")

    def test_login_method(self):
        '''test whether invalid user name error is returned when user enters invalid name'''
        results = self.new_user.login("mel", "123")
        self.assertEqual(results, 'welcome mel')

    def test_add_new_category_adds_new(self):
        '''tests whether the add new category method adds recipe category to category list'''
        self.new_category = RecipeCategories()
        results = self.new_category.add_new_category("snacks")
        self.assertEqual(results, ["snacks"])

    def test_view_category(self):
        '''test whether the method returns a list of existing recipe categories'''
        self.new_category = RecipeCategories()
        self.new_category.add_new_category("snacks")
        self.new_category.add_new_category("lunches")
        results = self.new_category.view_category()
        self.assertEqual(results, ["snacks","lunches"])

    def test_delete_category(self):
        '''tests whether the delete category actually deletes recipe categories'''
        self.new_category = RecipeCategories()
        self.new_category.add_new_category("snacks")
        self.new_category.add_new_category("lunches")
        results = self.new_category.delete_category("snacks")
        self.assertEqual(results, ["lunches"])

    def test_update_category(self):
        '''test whether the user is allowed to change category details'''
        self.new_category = RecipeCategories()
        self.new_category.add_new_category("snacks")
        self.new_category.add_new_category("lunches")
        self.new_category.update_category("lunches", "lunch")
        self.assertIn("lunch", self.defaultcategories)

    def test_add_new_recipe(self):
        '''tests whether a new recipe is added when method add_new_recipe is called '''
        self.new_recipe = Recipe()
        self.new_recipe.add_new_recipe("lunches", "githeri", "water maize beans", "mix")
        self.assertIn("mix", self.new_recipe.defaultrecipe)
    
    def test_view_recipe(self):
        self.new_recipe = Recipe()
        results = self.new_recipe.add_new_recipe("lunches", "githeri", "water maize beans", "mix")
        self.assertIn(":", results)


if __name__ == "__main__":
    unittest.main()