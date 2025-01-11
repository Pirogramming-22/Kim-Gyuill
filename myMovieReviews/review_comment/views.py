from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MovieReview
from .forms import MovieReviewForm
from real_comment.models import Comment


def main(request):
    sort_option = request.GET.get('sort', 'date')

    if sort_option == 'name':
        comments = MovieReview.objects.order_by('title')
    elif sort_option == 'rating':
        comments = MovieReview.objects.order_by('-rating')
    else:
        comments = MovieReview.objects.order_by('-created_at')  # 게시순

    context = {
        'comments': comments,
        'current_sort': sort_option,  # 현재 정렬 옵션 전달
    }
    return render(request, 'list.html', context)

def comment_create(request):
    if request.method == "POST":
        form = MovieReviewForm(request.POST, request.FILES)

        # 입력 예외처리
        if form.is_valid():
            comment = form.save()
            return redirect(reverse('comment:comment_detail', args=[comment.pk]))
        else:
            return render(request, 'review.html', {'form': form})
    form = MovieReviewForm()
    return render(request, 'review.html', {'form': form})

def comment_detail(request, pk):
    comments = MovieReview.objects.get(id=pk)
    runtime_filter = f"{comments.runtime // 60}시간 {comments.runtime % 60}분"
    real_comments = Comment.objects.filter(board=comments)
    context = {
        'comment': comments,
        'runtime_filter': runtime_filter,
        'real_comments': real_comments,
    }
    return render(request, 'detail.html', context)

def comment_update(request, pk):
    comment = get_object_or_404(MovieReview, pk=pk)
    if request.method == "POST":
        form = MovieReviewForm(request.POST, request.FILES, instance=comment)

        # 입력 예외처리
        if form.is_valid():
            form.save()
            return redirect(reverse('comment:comment_detail', args=[comment.pk]))
        else:
            return render(request, 'review.html', {'form': form, 'comment': comment})
    form = MovieReviewForm(instance=comment)
    return render(request, 'review.html', {'form': form, 'comment': comment})

def comment_delete(request, pk):
    if request.method == "POST":
        comment = MovieReview.objects.get(id=pk)
        comment.delete()
        return redirect('comment:main')
    return render(request, 'review.html')