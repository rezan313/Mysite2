from django.urls import reverse
from django.db import models
import uuid
class Genre(models.Model):
    name=models.CharField(max_length=300,help_text='enter a bokk genre')
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=300)
    author=models.ForeignKey('author',on_delete=models.SET_NULL,null=True)
    summary=models.CharField(max_length=300)
    isbn=models.CharField('ISbn',max_length=13,help_text='13 character')
    genre=models.ManyToManyField(Genre,help_text='select a genre for this book')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('app1:book_detail',args=[str(self.id)])
    def display_genre(self):
        return  reverse('app1:book_detail',args=[str(self.id)])
    display_genre.short_description = 'Genre'
class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='uniq Id for this')
    book=models.ForeignKey('book',on_delete=models.SET_NULL,null=True)
    imprint=models.CharField('imprint',max_length=300,null=True,blank=True)
    due_back=models.DateField(null=True,blank=True)
    LOAN_STATUS =   (
        ('m','Maintenance'),
        ('o','on loan'),
        ('a','Availble'),
        ('r','Revereved'),
    )
    status=models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='book availblity')
    class Meta:
        ordering=["due_back"]
    def __str__(self):
        return '%s (%s)'%(self.id,self.book.title)
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death = models.DateField('died',null=True, blank=True)
    def get_absolute_url(self):
        return reverse('app1:author_detail',args=[str(self.id)])
    def __str__(self):
        return '%s , %s'%(self.first_name,self.last_name)