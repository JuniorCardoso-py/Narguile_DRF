from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    SIZE = (
        ("P", 'Pequena'),
        ("M", 'Media'),
        ("G", 'Grande')
    )

    name = models.CharField(max_length=1, choices=SIZE)

    def __str__(self) -> str:
        return self.name
