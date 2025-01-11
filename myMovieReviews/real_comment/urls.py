from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'real_comment'

urlpatterns = [
    # 댓글 작성
    path('real_comment/<int:pk>/create', real_comment_create, name='real_comment_create'),

    # 댓글 삭제
    path('real_comment/<int:pk>', real_comment_delete, name='real_comment_delete'),

]