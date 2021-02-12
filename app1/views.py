from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre

def index(request):
    num_books=Book.objects.all().count()
    num_instance=BookInstance.objects.all().count()
    num_instance_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()

    return render(
        request,'app1/index.html',
        context={'num_books': num_books,'num_instance':num_instance,
                 'num_instance_available':num_instance_available,'num_authors':num_authors}

    )


# Create your views here.
