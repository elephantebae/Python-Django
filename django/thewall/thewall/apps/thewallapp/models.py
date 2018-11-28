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
        
class MessagesManager(models.Manager):
    def message_validator(self,postData):
        errors= {}
        if len(postData['mtext']) <0:
            errors['message'] = "Must have message to post message"
        return errors

class CommentsManager(models.Manager):
    def comment_validator(self,postData):
        errors={}
        if len(postData['ctext']) <0:
            errors['comments'] = "Must have a comment to post a comment"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length= 45)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Messages(models.Model):
    message= models.TextField()
    users_who_message= models.ForeignKey(Users, related_name="messages_from_users")
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    objects= MessagesManager()

class Comments(models.Model):
    comment= models.TextField()
    message_with_comments= models.ForeignKey(Messages, related_name="msg_comments")
    users_who_comments=models.ForeignKey(Users, related_name="user_comments")
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    objects= CommentsManager()

