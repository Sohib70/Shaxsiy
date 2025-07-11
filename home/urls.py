from .views import get_home,about,contact,blog
from django.urls import path

urlpatterns = [
    path('',get_home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),

]