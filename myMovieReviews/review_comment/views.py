from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MovieReview

def comment_create(request):

    # GET 요청 시 폼 템플릿 렌더링
    return render(request, 'review.html')
