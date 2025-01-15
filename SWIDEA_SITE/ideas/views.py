from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Idea
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def main(request):
    sort_option = request.GET.get('sort', 'newest')  # 기본 정렬 기준: 최신순
    title_filter = request.GET.get('title', '')

    ideas = Idea.objects.all()

    # 필터링
    if title_filter:
        ideas = ideas.filter(title__icontains=title_filter)

    # 정렬
    if sort_option == 'popularity':  # 관심도순
        ideas = ideas.order_by('-interest')
    elif sort_option == 'newest':  # 최신순
        ideas = ideas.order_by('-id')
    elif sort_option == 'oldest':  # 등록순
        ideas = ideas.order_by('id')
    elif sort_option == 'name_asc':  # 이름순
        ideas = ideas.order_by('title')
    elif sort_option == 'liked':  # 찜하기순
        ideas = ideas.order_by('-is_liked')

    paginator = Paginator(ideas, 4)  # 페이지당 4개의 아이디어
    page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기
    page_obj = paginator.get_page(page_number)  # 해당 페이지의 아이디어 가져오기

    # 예상 개발 툴 목록 추출 (중복 제거)
    devtools = Idea.objects.values_list('devtool', flat=True).distinct()

    context = {
        'page_obj': page_obj,
        'sort_option': sort_option,
        'devtools': devtools  # 예상 개발 툴 목록 전달
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