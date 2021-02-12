from django.urls import include
from django.contrib import admin
from django.conf.urls import url
from . import views
app_name='app1'
urlpatterns = [
 url(r'^$',views.index,name='index'),
 url(r'admin/', admin.site.urls),

]
