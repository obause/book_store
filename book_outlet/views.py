from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    all_books = Book.objects.all().order_by("title")
    num_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": all_books,
        "total_number_books": num_books,
        "average_rating": avg_rating,
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except Exception as e:
    #     raise Http404(e)
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
