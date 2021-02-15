from django.urls import include
from django.contrib import admin
from django.conf.urls import url
from . import views


app_name='app1'
urlpatterns = [
 url(r'^$',views.index.as_view(),name='index'),
 url(r'^books/$',views.BookListView.as_view(),name='books'),
 url(r'^book/(?P<pk>\d+)$',views.BookDetailView.as_view(),name='book_detail'),
url(r'^authors',views.AuthorListView.as_view(),name='authors')
]
