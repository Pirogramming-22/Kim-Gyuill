from django.urls import path
from board import views
from .views import *

app_name = 'board'

urlpatterns = [    
    path('', profile_page, name="profile_page"),
    path('upload/', upload_page, name="upload_page"),
    path('detail/<int:pk>', detail_page, name="detail_page"),
    path('like_post/', like_post, name='like_post'),
    path('search/', search_page, name='search_page'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('edit/<int:pk>/', edit_post, name='edit_post'),

] 