
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('post_listing/',post_listing,name='post_listing'),
    path('new/',new,name='new'),
    
]
