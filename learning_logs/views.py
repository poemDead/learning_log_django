from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

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
