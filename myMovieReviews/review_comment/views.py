from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MovieReview

def main(request):
    comments =  MovieReview.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'list.html', context)

def comment_create(request):
    if request.method == "POST":
        comment = MovieReview.objects.create(
            title=request.POST['title'],
            released_year=request.POST['year'],
            genre = request.POST['genre'],
            rating=request.POST['rating'],
            runtime=request.POST['runtime'],
            review=request.POST['review'],
            director=request.POST['director'],
            actor=request.POST['actor'],
        )
        return redirect(reverse('comment:comment_detail', args=[comment.pk]))
    return render(request, 'review.html')

def comment_detail(request, pk):
    comments = MovieReview.objects.get(id=pk)
    context = {
        'comment': comments,
    }
    return render(request, 'detail.html', context)

def comment_update(request, pk):


    return render(request, 'review.html')

def comment_delete(request, pk):
    if request.method == "POST":
        comment = MovieReview.objects.get(id=pk)
        comment.delete()
        return redirect('comment:main')
    return render(request, 'review.html')

