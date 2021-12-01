from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg
# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    number_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
    "books" : books,
    "total_number_of_books": number_books,
    "average_rating": avg_rating
    })


def book_details(request, slug):
    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug ) # this function replace the function above
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_best": book.is_best

    })