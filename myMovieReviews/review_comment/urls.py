from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'comment'

urlpatterns = [

    # 메인
    path('', main, name='main'),

    # 글 쓰기
    path('create', comment_create, name='comment_create'),

    # 디테일
    path('detail/<int:pk>', comment_detail, name='comment_detail'),

    # 업데이트
    path('upadte/<int:pk>', comment_update, name='comment_update'),

    # 삭제
    path('delete/<int:pk>', comment_delete, name='comment_delete'),

]