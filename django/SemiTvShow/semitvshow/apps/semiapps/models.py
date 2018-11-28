from __future__ import unicode_literals
from django.db import models

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {
        }
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"
        if len(Shows.objects.filter(title= postData['title']) > 0: 
            errors["titlerepeat"] = "Title already exists"
        if len(postData['network']) < 3:
            errors["network"] = "network name should be at least 3 characters"
        if len(postData['desc']) <10:
            errors['desc'] = "description name should be at least 10 characters"
        return errors
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length= 50)
    release_date= models.DateTimeField()
    desc = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = ShowsManager()
