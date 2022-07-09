from django.contrib import admin
from django.urls import path , include
from .import views
urlpatterns = [
    path('postcomment', views.postcomment, name='comment'),
    path('', views.bloghome, name='bloghome'),
    
    path('<str:slug>', views.blogpost, name='blogpost')
    # api to post a comment
    
]
