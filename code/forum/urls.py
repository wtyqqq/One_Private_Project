"""ForumSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^all/', views.all_tie),  # 全部帖子
    path(r'', views.home),
    url(r'^all-(?P<kid>\d+)-(?P<reply_limit>\d+)-(?P<time_limit>\d+)', views.all_tie),  # 按条件搜索帖子
    path('home/', views.home),  # 主页
    path('login/', views.login),  # 登录注册
    path('publish/', views.publish),  # 发布帖子
    url(r'^single/(?P<tid>\d+)/', views.single),  # 单个帖子
    path('edit-pwd/', views.edit_pwd),  # 修改密码
    path('my-admin/', views.admin),  # 修改密码
    path('announcement/', views.announcement),  # 公告管理
    path('admin-home/', views.topic_manage),  # 帖子管理，也是主页面
    path('kind-manage/', views.kind_manage),  # 板块管理
    url(r'^single-an-(?P<aid>\d+)/', views.single_an),  # 单个公告显示
    #用户未登录
    path('error/', views.error),
]
