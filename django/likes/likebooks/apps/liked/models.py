from django.db import models

class Users(models.Model):
    first_name =models.CharField(max_length = 255)
    last_name= models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)

class Books(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    uploaded_by = models.ForeignKey(Users, related_name="books_uploaded")
    users_who_likes = models.ManyToManyField(Users, related_name="liked_books")
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {} {} >".format(self.name, self.desc)
# Create your models here.
