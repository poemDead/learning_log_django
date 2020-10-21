from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EnrtyFrom

# Create your views here.
def index(request):
    """学习笔记应用的主页"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics,}
    return render(request, 'learning_logs/index.html', context)

def topic(request,topic_id):
    """显示单个主题下的所有笔记"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # create a new form
        form = TopicForm()
    else:
        # 如果是post请求，就提交表单处理数据，跳回topics界面
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:index')
    #如果没有post请求，就显示空表单
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # create a new form
        form = EnrtyFrom()
    else:
        # 如果是post请求，就提交表单处理数据，跳回topics界面
        form = EnrtyFrom(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    #如果没有post请求，就显示空表单
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """编辑已有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EnrtyFrom(instance=entry)
    else:
        form = EnrtyFrom(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)