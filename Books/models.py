from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.category

class BookModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/',blank=True)
    description = models.TextField()
    borrowingPrice = models.DecimalField(decimal_places=2,max_digits=5)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class BookReviewModel(models.Model):
    reviewer=models.CharField(max_length=100)
    review = models.TextField(max_length=200)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.book.name
    

class BookBorrow(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    borrower = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.book.name