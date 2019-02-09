from django.db import models

# Create your models here
# class author(models.Models):

#   author_id = models.IntegerField(primary_key = True)
#   author_name = models.CharField(max_length=100)

class Book(models.Model):

    BOOK_CATEGORY = (('suspense','suspense'),
                        ('crime','crime'),
                        ('thriller','thriller'),
                        ('tragedy','tragedy'),
                        ('fiction','fiction'))
        

    book_id = models.IntegerField(primary_key = True)
    book_name = models.CharField(max_length = 100)
    publish_date = models.DateField()
    category = models.CharField(max_length = 50, choices = BOOK_CATEGORY)
    book_author = models.CharField(max_length = 1000)

