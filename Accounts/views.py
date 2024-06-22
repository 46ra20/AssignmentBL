from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .forms import UserCreationForms,AmountForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm


from django.conf import settings
from django.core.mail import send_mail

# from .models import DepositModels

# Create your views here.

def UserCreationView(request):
    if request.method =='POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password1']
            
            user = authenticate(request=request,username=username,password=password)
            login(request,user)
            return redirect('homepage')
    form = UserCreationForms()
    return render(request,'Accounts/singup.html',{'form':form,'type':'Registration Form'})




def UserLoginView(request):
    if request.method =='POST':
       
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            form = login(request,user)
            return redirect('homepage')
    form = AuthenticationForm()
    return render(request,'Accounts/singup.html',{'form':form,'type':'Login Form'})


def UserLogoutView(request):
    logout(request)
    return redirect('homepage')


def DepositMoneyView(request):
    if request.method =='POST':
        form = AmountForm(request.POST)
        account = request.user.account
        amount = form.data['amount']

        account.deposit+=int(amount)

        account.save(
            update_fields=['deposit']
        )

        subject = 'Deposit Money in your Account'
        message = f'Hi {request.user.first_name} {request.user.last_name}, your money deposit successfully. Amount: {amount}$, Total Balance {account.deposit}$'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email]
        send_mail( subject, message, email_from, recipient_list )
    
    form = AmountForm()
    return render(request,"Accounts/deposit.html",{"form":form})