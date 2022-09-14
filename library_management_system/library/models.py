from django.db import models

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    no_of_books = models.IntegerField(null=True)

    def __str__(self):
        return self.title