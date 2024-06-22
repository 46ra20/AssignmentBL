from django.shortcuts import render
from django.http import HttpResponse
from Books.models import CategoryModel,BookModel,BookReviewModel,BookBorrow
from Books.forms import BookReviewForms
# Create your views here.

from django.shortcuts import render

def HomePage(request):
    category = CategoryModel.objects.all()
    books = BookModel.objects.all()
    # print(category,books)
    return render(request,'home.html',{'categorys':category,'books':books})

def ViewByCategory(request,id):
    categorys = CategoryModel.objects.all()
    books = BookModel.objects.filter(category=id)
    return render(request,'home.html',{'categorys':categorys,'books':books})


def ViewDetails(request,id):
    book = BookModel.objects.get(pk=id)
    review = BookReviewModel.objects.filter(book=id)
    
    if request.method=='POST':
        form = BookReviewForms(request.POST)
        BookReviewModel.objects.create(
            reviewer=request.user.first_name+' '+request.user.last_name,
            review=form.data['review'],
            book=book
        )
    form = BookReviewForms()
    return render(request,'detailsview.html',{'book':book,'form':form,'reviews':review})



def BookBorrowView(request):
    books = BookBorrow.objects.all()

    return render(request,'profile.html',{'books':books})