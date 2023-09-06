from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.db.models import Q

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
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)
