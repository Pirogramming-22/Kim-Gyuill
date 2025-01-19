from django.urls import path
from board import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'board'

urlpatterns = [    
    path('', profile_page, name="profile_page"),
    path('upload/', upload_page, name="upload_page"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)