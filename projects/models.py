from django.db import models

# Create your models here.

class Post(models.Model):

    title= models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField(upload_to="media",blank=True)

    def __str__(self):

        return self.title