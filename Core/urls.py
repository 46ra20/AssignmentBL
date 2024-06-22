from django.urls import path
from .views import HomePage,ViewByCategory,ViewDetails,BookBorrowView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',HomePage,name='homepage'),
    path('profile/',BookBorrowView,name='profile'),
    path('category/<int:id>',ViewByCategory,name='viewByCategory'),
    path('book/<int:id>',ViewDetails,name='detailsview'),
    
]

urlpatterns += staticfiles_urlpatterns()
