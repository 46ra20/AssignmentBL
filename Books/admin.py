from django.contrib import admin
from .models import CategoryModel,BookModel,BookReviewModel,BookBorrow

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(BookModel)
admin.site.register(BookReviewModel)
admin.site.register(BookBorrow)
