from django.shortcuts import render, redirect
from books.forms import BookForm
from .models import Book

# Create your views here.
def create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
        return redirect("books:detail", book.pk)
    else:
        form = BookForm()
    context = {
        "form": form,
    }
    return render(request, "books/create.html", context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book,
    }
    return render(request, "books/detail.html", context)


def correct(request):
    return render(request, "books/book_correct.html")


def incorrect(request):
    return render(request, "books/book_incorrect.html")
