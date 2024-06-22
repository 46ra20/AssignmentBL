from django.shortcuts import render,redirect
from .models import BookModel,BookBorrow

from django.conf import settings
from django.core.mail import send_mail

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

    subject = 'Borrow Book'
    message = f'Hi {request.user.first_name} {request.user.last_name}, you borrow this {book.name} book. Borrow Price: {book.borrowingPrice}$, After Borrow your balance {account.deposit}$, Thanks for using our service'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    send_mail( subject, message, email_from, recipient_list )

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
