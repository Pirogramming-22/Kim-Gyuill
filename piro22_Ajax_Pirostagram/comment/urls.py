from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('', views.comment_page, name="comment_page"),
    path('<int:pk>/', views.comment_page, name="comment_page_with_pk"),
]
