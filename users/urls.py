from django.urls import path,include

app_name = 'users'
urlpatterns = [
    # 使用django默认的身份验证url
    path('', include('django.contrib.auth.urls')),
    # 
]