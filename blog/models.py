from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    data=models.TextField()
    date=models.CharField(max_length=13)

    def __str__(self):
        return self.title