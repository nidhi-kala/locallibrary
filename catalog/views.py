from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Book, BookInstance, Author, Genre
from django.db.models import Q
from django.views import generic

# Create your views here.


def index(request):
    word = request.GET.get('word', '')
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres_with_word = Genre.objects.filter(name__icontains=word).count
    num_books_with_word = Book.objects.filter(
        Q(title__icontains=word) | Q(summary__icontains=word)).count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
