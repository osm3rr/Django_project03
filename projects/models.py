from django.db import models

# Create your models here.

class Post(models.Model):

    title= models.CharField(max_length=30)
    description=models.TextField()
    #image=models.ImageField()

    def __str__(self):

        return self.title