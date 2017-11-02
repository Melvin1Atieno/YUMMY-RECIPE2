class UserAccount(object):

    def __init__(self):
        self.userdetails = {}
        self.users = []

    def add_new(self, username, email, password, confirm_password):
        if email in self.users:
            return "the email is registered to an existing user"
        self.userdetails[username] = [username, email, password]
        self.users.append(email)
        return "ACCOUNT SUCCEFULLY CREATED"

    def confirm(self, username, password):
        if username not in self.userdetails:
            return "Invalid User name"
        userpassword = self.userdetails[username][2]
        if userpassword != password:
            return "incorrect password"
        return "welcome", username
    def login(self, username, password):
        self.confirm(username, password)


    # def view_details(self, username):
        # return username,":",self.userdetails[username]

    # def update(self,name):
        # pass
    # def delete(self, username):
        # del self.userdetails[name]

class RecipeCategories(object):

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

    def delete_category(self,name):
        '''deletes an existing recipe category'''
        if name in self.defaultcategories:
            self.defaultcategories.remove(name)
        else:
            return "category does not exist"

    def update_category(self,oldrecipecategory, newrecipecategory):
        '''updates an existing recipe category'''
        if oldrecipecategory in self.defaultcategories:
            self.defaultcategories.remove(oldrecipecategory)
            self.defaultcategories.append(newrecipecategory)
        else:
            return "category does not exist"

class Recipe(RecipeCategories):

    def __init__(self):
        '''calling the superclass'''
        super().__init__()
        self.defaultrecipe = {}
    
    def add_new_recipe(self, category, name, ingredients, method,):
        '''adds a new recipe'''
        self.defaultrecipe[name]=[[ingredients],method]
        if category not in self.defaultcategories:
            self.defaultcategories[category] = [name,":",self.defaultrecipe[name]]
        else:
            self.defaultcategories[category].append([name,":",self.defaultrecipe[name]])
    
    def view_recipe(self,recipename):
        '''allows user to see an existing recipe'''
        return recipename, ":", self.defaultrecipe[recipename]

    def delete_recipe(self,name):
        '''deletes an existing recipe'''
        pass
        
    
    def update_recipe(self,oldrecipe, newrecipe):
        RecipeCategories.update_category(self, oldrecipe, newrecipe)
        pass




