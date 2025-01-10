from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MovieReview
from .forms import MovieReviewForm

def main(request):
    comments =  MovieReview.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'list.html', context)

def comment_create(request):
    if request.method == "POST":
        form = MovieReviewForm(request.POST)

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
    context = {
        'comment': comments,
        'runtime_filter': runtime_filter,
    }
    return render(request, 'detail.html', context)

def comment_update(request, pk):
    comment = get_object_or_404(MovieReview, pk=pk)
    if request.method == "POST":
        form = MovieReviewForm(request.POST, instance=comment)

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