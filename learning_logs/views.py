from django.shortcuts import render
from .models import Topic

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