from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PostForm
from .models import Board
from comment.models import  Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

def detail_page(request, pk):
    post = Board.objects.get(id=pk)
    comments_count = Comment.objects.filter(board=post).count()
    context = {
        'post': post,
        'comments_count': comments_count
    }
    return render(request, 'detail.html', context)

@csrf_exempt
def like_post(request):
    req = json.loads(request.body)
    board_id = req['id']
    button_type = req['type']

    board = Board.objects.get(id=board_id)

    if button_type == 'like':
        board.like += 1
    board.save()

    return JsonResponse({'id':board_id, 'type':button_type})

def search_page(request):
    boards = Board.objects.all()
    return render(request, 'search.html', {'boards': boards})