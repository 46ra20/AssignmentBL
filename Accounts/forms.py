from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import DepositModels



class UserCreationForms(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name']
    
    def save(self,commit=True):
        current_user = super().save(commit=False)
        if commit==True:
            current_user.save()
        DepositModels.objects.create(
            user=current_user
        )
        return current_user


class AmountForm(forms.Form):
    amount = forms.DecimalField(max_digits=12,decimal_places=2)