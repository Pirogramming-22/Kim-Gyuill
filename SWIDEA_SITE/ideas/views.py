from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Idea
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# 메인 페이지 (아이디어 목록)
def main(request):
    ideas = Idea.objects.all()  # 모든 아이디어 가져오기
    paginator = Paginator(ideas, 4)  # 페이지당 최대 4개
    page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기
    page_obj = paginator.get_page(page_number)  # 해당 페이지의 아이디어 가져오기

    context = {
        'page_obj': page_obj  # 페이지네이션 객체를 템플릿에 전달
    }
    return render(request, 'list.html', context)

# 아이디어 생성
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

# 아이디어 상세보기
def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea': idea
    }
    return render(request, 'detail.html', context)

# 아이디어 수정
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

# 아이디어 삭제
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        idea.delete() 
        return redirect('ideas:main')
    return redirect('ideas:idea_detail', pk=pk)

def toggle_like(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        idea.is_liked = not idea.is_liked
        idea.save()
        print(f"Idea {pk} liked status toggled to {idea.is_liked}")  # 디버깅용
        return JsonResponse({"is_liked": idea.is_liked})
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def update_interest(request, pk):
    if request.method == "POST":
        try:
            idea = Idea.objects.get(pk=pk)
            data = json.loads(request.body)
            increment = data.get('increment', True)
            if increment:
                idea.interest += 1
            else:
                idea.interest = max(0, idea.interest - 1)  # 관심도가 음수가 되지 않도록 설정
            idea.save()
            return JsonResponse({'success': True, 'new_interest': idea.interest})
        except Idea.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Idea not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})