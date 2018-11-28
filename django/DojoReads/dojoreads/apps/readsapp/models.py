from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class UsersManager(models.Manager):
    def register_validator(self, postData):
        errors= {}
        if len(postData['name']) <2:
            errors["name"]= "First Name must be at least 2 characters."
        elif postData['name'].isalpha() is False:
            errors["name"]= "First Name must be letters."
        if len(postData['alias']) <2:
            errors['alias']= "Last Name must be at least 2 characters."
        elif postData['alias'].isalpha() is False:
            errors["alias"]= "Last Name must be letters."
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors["email"]= "email is not in format!"
        if len(Users.objects.filter(email=postData['email'])) > 0:
            errors["email"]= "this email already exists please try again." 
        if len(postData['password']) <8:
            errors["password"]="password must be at least 8 characters."
        if postData['password'] != postData['cpw']:
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

class Users(models.Model):
    name = models.CharField(max_length= 45)
    alias = models.CharField(max_length = 45)
    email = models.CharField(max_length= 255)
    password = models.CharField(max_length =45)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()

class Books(models.Model):
    title = models.CharField(max_length=45)
    author= models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class Reviews(models.Model):
    review = models.TextField()
    rating= models.FloatField()
    users_who_reviewed = models.ForeignKey(Users, related_name="reviews_from_user")
    books_reviewed= models.ForeignKey(Books, related_name="reviews_for_book")
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now=True)