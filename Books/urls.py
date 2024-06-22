from django.urls import path
from .views import BorrowBook,ReturnBookView

urlpatterns = [
    path('borrowbook/<int:id>',BorrowBook,name='borrowbook'),
    path('returnbook/<int:id>',ReturnBookView,name='returnbook')
]
