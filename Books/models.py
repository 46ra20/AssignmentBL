from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.category

class BookModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    description = models.TextField()
    borrowingPrice = models.DecimalField(decimal_places=2,max_digits=5)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name