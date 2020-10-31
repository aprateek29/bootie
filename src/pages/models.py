from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/')
    price = models.IntegerField()
    rating = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    @property
    def get_rating(self):
        return self.rating

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name