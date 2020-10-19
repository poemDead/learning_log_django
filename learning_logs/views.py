from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """学习笔记应用的主页"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics,}
    return render(request, 'learning_logs/index.html', context)