
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('post_listing/',post_listing,name='post_listing'),
    path('compose_post/',compose_post,name='compose_post'),
    path('post_delete/<int:id>/',post_delete,name='post_delete'),
    path('register/',register,name='register'),
    path('comment_on_post/<int:id>/',comment_on_post,name='comment_on_post'),
    path('like/<int:id>/',like,name='like'),
    path('logout/',logout,name='logout'),
    path('post_with_comment/<int:id>/',post_with_comment,name='post_with_comment'),
    path('delete_comment/<int:id>/',delete_comment,name='delete_comment'),
   

    
]
