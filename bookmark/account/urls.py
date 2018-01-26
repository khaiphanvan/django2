from django.urls import path, include
from django.contrib.auth.views import login, logout,logout_then_login,password_change,password_change_done,\
                                        password_reset,password_reset_done,password_reset_confirm,password_reset_complete
#from django.urls.conf import include
from . import views


urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    # login / logout urls
    # path('', views.user_login, name='index'),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    # change password urls
    path('password-change/', password_change, name='password_change'),
    path('password-change/done/', password_change_done, name='password_change_done'),

    # restore password urls
    path('password-reset/', password_reset, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', password_reset_complete, name='password_reset_complete'),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
