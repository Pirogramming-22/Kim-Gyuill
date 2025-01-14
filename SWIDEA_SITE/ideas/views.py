from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Idea
from .forms import PostForm

# Create your views here.
def main(request):

    return render(request, 'list.html')

def idea_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        # # 입력 예외처리
        # if form.is_valid():
        #     comment = form.save()
        #     return redirect(reverse('ideas:idea_detail', args=[comment.pk]))
        # else:
        #     return render(request, 'register.html', {'form': form})
    form = PostForm()
    return render(request, 'register.html', {'form': form})