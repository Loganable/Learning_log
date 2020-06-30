"""为应用程序users定义URL模式"""

from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面
    re_path('^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    
    # 注销
    re_path('^logout/$', views.logout_view, name='logout'),
    
    # 注册页面
    re_path('^register/$', views.register, name='register')
]

app_name = 'users'