from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Comment, Board

def comment_page(request, pk):
    post = get_object_or_404(Board, id=pk)
    comments = Comment.objects.filter(board=post, parent__isnull=True).order_by('-created_at')  # 부모 댓글만 가져오기
    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        if content:
            parent_comment = None
            if parent_id:
                parent_comment = get_object_or_404(Comment, pk=parent_id)
            Comment.objects.create(board=post, content=content, parent=parent_comment)
            return redirect('comment:comment_page_with_pk', pk=post.id)
    return render(request, 'comment.html', {'post': post, 'comments': comments})


def delete_comment(request, pk):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=pk)
        board_pk = comment.board.id
        comment.delete()
        return redirect('comment:comment_page_with_pk', pk=board_pk)
    

def delete_reply(request, pk):
    if request.method == "POST":
        reply = get_object_or_404(Comment, pk=pk)
        parent_comment = reply.parent
        reply.delete()
        return redirect('comment:comment_page_with_pk', pk=parent_comment.board.id)