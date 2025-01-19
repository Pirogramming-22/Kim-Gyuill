from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PostForm
from .models import Board

def profile_page(request):
    boards = Board.objects.all()  # 모든 게시물 가져오기
    return render(request, 'profile.html', {'boards': boards})

def upload_page(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('board:profile_page'))
        else:
            return render(request, 'upload.html', {'form': form})

    # GET 요청인 경우 빈 폼을 생성
    form = PostForm()
    return render(request, 'upload.html', {'form': form})
