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
    comments = MovieReview.objects.get(id=pk)
    context = {
        'comment': comments,
    }
    return render(request, 'detail.html', context)

def comment_update(request, pk):
    # 객체 가져오기 (존재하지 않으면 404 반환)
    comment = get_object_or_404(MovieReview, id=pk)

    if request.method == "POST":
        # 폼에 데이터 바인딩 (기존 데이터 + 새로운 POST 데이터)
        form = MovieReviewForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment:comment_detail', pk=comment.pk)
    else:
        # GET 요청: 기존 데이터를 폼에 바인딩
        form = MovieReviewForm(instance=comment)

    # review.html로 렌더링
    return render(request, 'review.html', {'form': form})
