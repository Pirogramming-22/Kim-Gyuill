from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MovieReview
from .forms import MovieReviewForm

def main(request):
    return render(request, 'list.html')

def comment_create(request):
    if request.method == "POST":
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect(reverse('comment:comment_detail', args=[comment.pk]))
        else:
            return render(request, 'review.html', {'form': form})
    else:
        # GET 요청 시 빈 폼 렌더링
        form = MovieReviewForm()
    return render(request, 'review.html', {'form': form})

def comment_detail(request, pk):
    comments = MovieReview.objects.get(pk=pk)
    context = {
        'comment': comments,
    }
    return render(request, 'detail.html', context)

