from django.urls import path
from ideas import views
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'tools'

urlpatterns = [    

    # 메인
    path('', tools_list, name='tools_list'),

    # 폼 생성
    path('create', tools_create, name='tools_create'),

    # 폼 디테일
    path('detail/<int:pk>', tools_detail, name='tools_detail'),
    
    # 폼 업데이트
    path('update/<int:pk>', tools_update, name='tools_update'),

    # 폼 삭제
    path('delete/<int:pk>', tools_delete, name='tools_delete'),

]