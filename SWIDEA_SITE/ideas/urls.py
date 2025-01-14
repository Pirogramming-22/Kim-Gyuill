from django.urls import path
from ideas import views
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = 'ideas'

urlpatterns = [    
    # 메인
    path('', main, name='main'),

    # 아이디어어 쓰기
    path('create', idea_create, name='idea_create'),
]