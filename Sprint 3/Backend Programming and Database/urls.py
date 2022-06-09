from django.urls import path
from django.contrib import admin
from django.urls.resolvers import URLPattern
from . import views

#URLConf
urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('basepage/',views.basepage, name = 'old_home'),
    path('base/', views.homepage, name ='homepage'),
    path('test/', views.about, name = 'about'),
    path('helpdesk/', views.helpdesk, name = 'helpdesk'),
    path('updates/', views.updates, name = 'latest_updates'),
    path('a_test/', views.a_test, name = 'a_test'),
    path('home/', views.login_home, name = 'login_home'),
    path('sharespaces/', views.sharespaces, name = 'sharespaces'),
    path('ShareMessage/', views.sharemessage, name = 'sharemessage'),
    path('login/', views.login, name ='login'),
    path('register/', views.register, name = 'register'),
]  