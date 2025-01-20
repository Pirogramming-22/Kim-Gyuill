from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm
from .models import Board
from comment.models import Comment
import json

# 프로필 페이지
def profile_page(request):
    boards = Board.objects.all()  # 모든 게시물 가져오기
    return render(request, 'profile.html', {'boards': boards})

# 게시글 업로드 페이지
def upload_page(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('board:profile_page'))
    else:
        form = PostForm()

    return render(request, 'upload.html', {'form': form, 'post': None})

# 게시글 상세 페이지
def detail_page(request, pk):
    post = get_object_or_404(Board, id=pk)
    comments_count = Comment.objects.filter(board=post).count()
    context = {
        'post': post,
        'comments_count': comments_count
    }
    return render(request, 'detail.html', context)

# 게시글 수정 페이지
def edit_post(request, pk):
    post = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('board:detail_page', args=[pk]))
    else:
        form = PostForm(instance=post)

    return render(request, 'upload.html', {'form': form, 'post': post})

# 게시글 삭제
def delete_post(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Board, pk=pk)
        post.delete()  # 모델의 delete 메서드가 호출되어 이미지도 삭제됨
        return redirect(reverse('board:profile_page'))

# 좋아요 기능
@csrf_exempt
def like_post(request):
    req = json.loads(request.body)
    board_id = req['id']
    button_type = req['type']

    board = Board.objects.get(id=board_id)

    if button_type == 'like':
        board.like += 1
    board.save()

    return JsonResponse({'id': board_id, 'type': button_type})

# 검색 페이지
def search_page(request):
    boards = Board.objects.all()
    return render(request, 'search.html', {'boards': boards})
