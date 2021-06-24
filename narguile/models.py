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

    name = models.CharField(max_length=1, choices=SIZE, unique=True)

    def __str__(self) -> str:
        return self.name


# def validate_str(value):
#     if type(value) != str:
#         raise ValueError('Valor erraduuu')
#     return value

# def create_product(name,description,price,category):
#     validate_str(name)
#     return Product(
#         name=name,
#         description=description,
#         price=price,
#         category=category
#     )