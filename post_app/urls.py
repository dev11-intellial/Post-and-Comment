
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('post_listing/',post_listing,name='post_listing'),
    path('user_post/',user_post,name='user_post'),
    path('compose_post/',compose_post,name='compose_post'),
    path('sucess/',sucess,name='sucess'),
    path('post_delete/<int:id>/',post_delete,name='post_delete'),
    path('register/',register,name='register'),
    
]
