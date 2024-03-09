"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from webapp01 import views
from django.conf.urls.static import static
from . import settings
from django.conf.urls.static import static
 
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.hello),
    path('user/add', views.user_add),
    path('user/login', views.user_login),
    path('test/insert',views.insert),
    path('',views.welcome),
    path('delete/',views.delete),
    path('rw_delete/',views.rw_delete),
    path('js_rw/',views.js_rw),
    path('login_success',views.login_success),
    path('task/add',views.task_add),
    path('task_detail/',views.task_detail),
    path('task/mytask',views.task_mytask),
    path('clear_session',views.clear_session),
    path('del_js_rw/',views.del_js_rw),
    path('wc_rw/',views.wc_rw),
    path('userinfo/',views.userinfo1),
    path('search1',views.search1),
]
