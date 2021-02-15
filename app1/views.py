from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre
from django.views import generic
from . import models

class index(generic.TemplateView):
    template_name = 'app1/index.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['num_books']=models.Book.objects.all().count()
        context['num_instance']=models.BookInstance.objects.count()
        context['num_instance_available']=models.BookInstance.objects.filter(status__exact='a').count()
        context['num_authors'] = models.BookInstance.objects.filter(status__exact='a').count()
        return context
class BookListView(generic.ListView):
    model=models.Book
    template_name = 'app1/book_list.html'
class BookDetailView(generic.ListView):
    model=models.Book
    template_name ='app1/books_detail.html'



# Create your views here.
