from .models import BookReviewModel
from django.forms import ModelForm

class BookReviewForms(ModelForm):
    class Meta:
        model = BookReviewModel
        fields=['review']