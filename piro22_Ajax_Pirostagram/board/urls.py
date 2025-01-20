from django.urls import path
from board import views
from .views import *

app_name = 'board'

urlpatterns = [    
    path('', profile_page, name="profile_page"),
    path('upload/', upload_page, name="upload_page"),
    path('detail/<int:pk>', detail_page, name="detail_page"),
    path('like_post/', like_post, name='like_post'),

] 