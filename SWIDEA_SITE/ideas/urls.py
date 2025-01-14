from django.urls import path
from ideas import views
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = 'ideas'

urlpatterns = [    
    # 메인
    path('', main, name='main'),

    # 아이디어에 쓰기
    path('create', idea_create, name='idea_create'),

    # 디테일 페이지
    path('detail/<int:pk>', idea_detail, name='idea_detail' ),

    # 업데이트 페이지
    path('update/<int:pk>', idea_update, name='idea_update'),

    # 삭제제
    path('delete/<int:pk>', idea_delete, name='idea_delete'),

]