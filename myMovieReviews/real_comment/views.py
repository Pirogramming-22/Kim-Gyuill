from django.shortcuts import render
from .models import Comment
from .models import MovieReview
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


def real_comment_create(request, pk):
    if request.method == 'POST':
        boards = MovieReview.objects.get(id=pk)
        Comment.objects.create(
            board=boards,
            content=request.POST['content']
        )
        return redirect('comment:comment_detail', pk=boards.id)


def real_comment_delete(request, pk):
    if request.method == 'POST':
        comment = Comment.objects.get(id=pk)
        board_pk = comment.board.id
        comment.delete()
        return redirect('comment:comment_detail', pk=board_pk)