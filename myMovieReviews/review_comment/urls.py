from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'comment'

urlpatterns = [

    # 글 쓰기
    path('create', comment_create, name='comment_create'),
]