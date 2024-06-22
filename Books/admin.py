from django.contrib import admin
from .models import CategoryModel,BookModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(BookModel)
