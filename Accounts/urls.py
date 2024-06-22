from django.urls import path
from .views import UserCreationView,UserLoginView,UserLogoutView,DepositMoneyView

urlpatterns = [
    path('singup/',UserCreationView,name='singup'),
    path('login/',UserLoginView,name='login'),
    path('logout/',UserLogoutView,name='logout'),
    path('deposit/',DepositMoneyView,name='deposit'),
]
