class UserAccount(object):

    def __init__(self):
        self.userdetails = {}
        self.users = []

    def add_new(self, username, email, password):
        '''adds new user'''
        if email in self.users:
            return "exists"
        self.userdetails[username] = [username, email, password]
        self.users.append(email)
        return "success"

    def confirm(self, username, password):
        '''confirms correct username and password'''
        error = None
        if username not in self.userdetails:
            error = "Invalid User name"
            return error
        userpassword = self.userdetails[username][2]
        if userpassword != password:
            error = "incorrect password"
        return error

    def login(self, username, password):
        '''logs user in after their details have been confirmed'''
        if self.confirm(username, password) != None:
            return "SUCCESSFUL LOGIN"

    def view_details(self, username):
        '''returns a dict of the user details'''
        return self.userdetails[username]

    def update_details(self, username):
        '''takes in new variables to re[l] '''
        pass


class RecipeCategories(object): 
    '''recipe category class'''
    def __init__(self):
        self.defaultcategories = []

    def add_new_category(self, name):
        '''checks if the category exists, adds new recipe category if it doesn't '''
        if name in self.defaultcategories:
            return "The category entered already exists"
        else:
            self.defaultcategories.append(name)
            return self.defaultcategories

    def view_category(self):
        '''returns a list of recipe categories'''
        return self.defaultcategories

    def delete_category(self, name):
        '''deletes an existing recipe category'''
        if name in self.defaultcategories:
            self.defaultcategories.remove(name)
        else:
            return "category does not exist"

    def update_category(self, oldrecipecategory, newrecipecategory):
        '''updates an existing recipe category'''
        if oldrecipecategory in self.defaultcategories:
            self.defaultcategories.remove(oldrecipecategory)
            self.defaultcategories.append(newrecipecategory)
        else:
            return "category does not exist"

class Recipe(object):
    '''child class of the recipe category class'''

    def __init__(self):
        '''initializing the'''
        self.defaultrecipe = {}

    def add_new_recipe(self, recipename, ingredients, method,):
        '''adds a new recipe'''
        self.defaultrecipe[recipename]=[[ingredients], method]
        if recipename not in self.defaultrecipe:
            self.defaultrecipe = [[ingredients], method]
        return "recipe already exists"

    def view_recipe(self, recipename):
        '''allows user to see an existing recipe'''
        return self.defaultrecipe[recipename]

    def delete_recipe(self, recipename):
        '''deletes an existing recipe'''
        if recipename in self.defaultrecipe:
            del self.defaultrecipe[recipename]
        
    def update_recipe(self,oldrecipe, newrecipe):
        RecipeCategories.update_category(self, oldrecipe, newrecipe)
        pass




