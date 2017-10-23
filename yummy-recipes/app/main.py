# -*- coding:utf-8 -*-

class YummyRecipeRegistration(object):
    def __init__ (self):
        self.invalid =   ('''!," ",*,~[,<,>,&,",\,',=,\,\,\],~''')
        
    def get_firstname(self,firstname):
        self.firstname = firstname
        for letter in self.firstname:
            if letter in self.invalid:
                return "firstname should not contain any of these" ,self.invalid, "characters"
            else:
                pass
    def get_lastname(self,lastname):
        self.lastname = lastname
        for letter in self.lastname:
            if letter in self.invalid:
                return "last should not contain any of these" ,self.invalid, "characters"
            else:
                pass
    def get_username(self,username):
        self.username = username
        for letter in self.username:
            if letter in self.invalid:
                return "invalid username"
            else:
                pass


    def get_email(self,email):
        self.email = email
        for letter in self.email:
            if letter in self.invalid:
                return "email should not contain any of these" ,self.invalid, "characters"
            else:
                pass
    def get_password(self,password):
        self.password = password
        if len(self.password) < 8:
            return "password has to have more than 8 characters"
        elif " " in self.password:
            return "password should not contain spaces"
        else:
            pass
#class YummyAccountLogin(YummyRecipeRegistration):
 #   def __init__(self, username,password):
 #       super().__init__(username,password)
