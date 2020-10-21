from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # topic page
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # new topic page
    path('new_topic/', views.new_topic, name='new_topic'),
    # new entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # edit entry page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]