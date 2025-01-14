from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Idea
from .forms import PostForm

# Create your views here.
def main(request):
    ideas = Idea.objects.all()
    context = {
        'ideas' : ideas
    }
    return render(request, 'list.html', context)

def idea_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save() 
            return redirect(reverse('ideas:idea_detail', args=[idea.pk])) 
        else:
            return render(request, 'register.html', {'form': form})

    # GET 요청인 경우 빈 폼을 생성
    form = PostForm()
    return render(request, 'register.html', {'form': form})

def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea' : idea
    }
    return render(request, 'detail.html', context)

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=idea)

        if form.is_valid():
            if not form.cleaned_data.get('image') and idea.image:
                form.instance.image = idea.image
            form.save()
            return redirect(reverse('ideas:idea_detail', args=[idea.pk]))
        else:
            return render(request, 'register.html', {'form': form, 'idea': idea})
    form = PostForm(instance=idea)
    return render(request, 'register.html', {'form': form, 'idea': idea})



def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        idea.delete() 
        return redirect('ideas:main')
    return redirect('ideas:idea_detail', pk=pk)