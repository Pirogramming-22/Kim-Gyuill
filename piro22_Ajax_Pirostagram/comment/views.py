from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Comment, Board

def comment_page(request, pk):
    post = get_object_or_404(Board, id=pk)
    comments = Comment.objects.filter(board=post).order_by('-created_at')
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(board=post, content=content)
            return redirect('comment:comment_page_with_pk', pk=post.id)
    return render(request, 'comment.html', {'post': post, 'comments': comments})


def delete_comment(request, pk):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=pk)
        board_pk = comment.board.id
        comment.delete()
        return redirect('comment:comment_page_with_pk', pk=board_pk)