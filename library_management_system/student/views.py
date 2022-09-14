from django.shortcuts import render
from django.http import HttpResponse
from library.models import Books
# Create your views here.


def allbooks(request):
    all_books = Books.objects.all()
    book_details = []
    for row in all_books:
        book_details.append({"title":row.title,"author":row.author,"status":row.status,"count":row.no_of_books})
    context = {"books":book_details}
    return render(request, 'student/books.html', context)
    # return HttpResponse(book_details)