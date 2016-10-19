from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from .models import Category, Book, Author
from .forms import BookForm


class BookList(ListView):
    queryset = Book.objects.all()
    context_object_name = 'book_list'
    template_name = 'books/list.html'


class BookDetail(DetailView):
    queryset = Book.objects.all()
    context_object_name = 'book'
    template_name = 'books/detail.html'


class AuthorBookList(BookList):

    def get_queryset(self):
        self.author = get_object_or_404(Author, id=self.args[0])
        return Book.objects.filter(author=self.author)


class BookCreate(CreateView):
    form_class = BookForm
    template_name = 'books/create.html'


class BookUpdate(UpdateView):
    queryset = Book.objects.all()
    form_class = BookForm
    template_name = 'books/update.html'
