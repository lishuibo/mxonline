"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from mxonline.settings import MEDIA_ROOT, STATICFILES_DIRS
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, \
    IndexView
import xadmin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    # path('login/', views.user_login, name='login'),
    # path('^login/', LoginUnsafeView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    # path('org_list/', OrgView.as_view(), name='org_list'),
    path('org/', include('organization.urls', namespace='org')),
    path("course/", include('course.urls', namespace="course")),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    path('users/', include('users.urls', namespace='users')),
    path('logout/', LogoutView.as_view(), name='logout'),
    re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_DIRS}),
    path('ueditor/', include('DjangoUeditor.urls')),
]
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'