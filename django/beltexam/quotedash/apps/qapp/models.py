from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class UsersManager(models.Manager):
    def register_validator(self, postData):
        errors= {}
        if len(postData['fname']) <2:
            errors["fname"]= "First Name must be at least 2 characters."
        elif postData['fname'].isalpha() is False:
            errors["fname"]= "First Name must be letters."
        if len(postData['lname']) <2:
            errors['lname']= "Last Name must be at least 2 characters."
        elif postData['lname'].isalpha() is False:
            errors["lname"]= "Last Name must be letters."
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors["email"]= "email is not in format!"
        if len(Users.objects.filter(email=postData['email'])) > 0:
            errors["email"]= "this email already exists please try again." 
        if len(postData['pw']) <8:
            errors["password"]="password must be at least 8 characters."
        if postData['pw'] != postData['cpw']:
            errors['password']= "password is not matching!"
        return errors

    def login_validator(self,postData):
        errors= {}
        if len(Users.objects.filter(email= postData['lemail'])) < 1:
            errors['lemail']= "email is not registered yet"
        else:
            if not bcrypt.checkpw(postData['lpassword'].encode(), Users.objects.get(email= postData['lemail']).password.encode()):
                errors['lpassword']="password does not match"
        return errors
    def edit_validator(self, postData):
        errors= {} 
        if len(postData['fnedit']) <1:
            errors['fnedit']= "Must have characters"
        if len(postData['lnedit']) <1:
            errors['lnedit']= "Must have characters"
        if len(postData['emedit']) <1:
            errors['emedit']= "Must have characters"
        elif not EMAIL_REGEX.match(postData['emedit']):    # test whether a field matches the pattern
            errors["emedit"]= "email is not in format!"
        return errors
class QuotesManager(models.Manager):
    def quote_validator(self,postData):
        errors = {}
        if len(postData['author']) <3:
            errors['author']= "Author must be more than 3 characters long"
        if len(postData['quote']) <10: 
            errors['quote']= "Quote must be more than 10 characters long"
        return errors
class Users(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length= 45)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=50)
    users_who_quote = models.ForeignKey(Users, related_name="quotes_from_user")
    likes = models.ManyToManyField(Users, related_name="users_who_likes")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= QuotesManager()

