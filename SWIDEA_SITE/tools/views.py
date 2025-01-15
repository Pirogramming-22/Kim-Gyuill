from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Tool
from .forms import ToolForm
from django.core.paginator import Paginator

# Create your views here.

# Create your views here.
def tools_list(request):
    tools = Tool.objects.all()
    paginator = Paginator(tools, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
    }
    return render(request, 'tool/tool_list.html', context)

def tools_create(request):
    if request.method == "POST":
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save() 
            return redirect(reverse('tools:tools_detail', args=[idea.pk])) 
        else:
            return render(request, 'tool/tool_register.html', {'form': form})

    # GET 요청인 경우 빈 폼을 생성
    form = ToolForm()
    return render(request, 'tool/tool_register.html', {'form': form})

# Tool detail view
def tools_detail(request, pk):
    tool = get_object_or_404(Tool, id=pk)
    context = {
        'tool': tool
    }
    return render(request, 'tool/tool_detail.html', context)

def tools_update(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == "POST":
        form = ToolForm(request.POST, request.FILES, instance=tool)

        if form.is_valid():
            form.save()
            return redirect(reverse('tools:tools_detail', args=[tool.pk]))
        else:
            return render(request, 'tool/tool_register.html', {'form': form, 'tool': tool})
    form = ToolForm(instance=tool)
    return render(request, 'tool/tool_register.html', {'form': form, 'tool': tool})

def tools_delete(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == "POST":
        tool.delete() 
        return redirect('tools:tools_list')
    return redirect('tools:tools_detail', pk=pk)