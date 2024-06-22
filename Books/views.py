from django.shortcuts import render,redirect
from .models import BookModel,BookBorrow

# Create your views here.


def BorrowBook(request,id):
    book = BookModel.objects.get(pk=id)
    account = request.user.account

    account.deposit -= book.borrowingPrice

    account.save(
        update_fields = ['deposit']
    )
    BookBorrow.objects.create(
        borrower=request.user,
        book=book
    )

    return redirect('profile')

def ReturnBookView(request,id):
    book = BookBorrow.objects.get(pk=id)

    account = request.user.account

    account.deposit += book.book.borrowingPrice

    account.save(
        update_fields = ['deposit']
    )
    book.delete()
    return redirect('profile')
