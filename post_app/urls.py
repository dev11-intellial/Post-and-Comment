
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('posts/',posts,name='posts'),
    path('compose_post/',compose_post,name='compose_post'),
    path('post_delete/<int:id>/',post_delete,name='post_delete'),
    path('register/',register,name='register'),
    path('comments/<int:id>/',comments,name='comments'),
    path('like/<int:id>/',like,name='like'),
    path('dislike/<int:id>/',dislike,name='dislike'),
    path('logout/',logout,name='logout'),
    path('delete_comment/<int:id>/',delete_comment,name='delete_comment'),
   

    
]
