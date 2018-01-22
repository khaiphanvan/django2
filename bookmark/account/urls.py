from django.urls import path, include
from django.contrib.auth.views import login, logout,logout_then_login
#from django.urls.conf import include
from . import views


urlpatterns = [
    # post views
    #path('login/', views.user_login, name='login'),
    # login / logout urls
    path('', views.user_login, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
]
