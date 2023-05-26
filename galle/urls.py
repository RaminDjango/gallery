from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('form-info', views.form, name='form'),
    path('login/', views.log, name='logins'),
    path('register/', views.register, name='regist'), 
    path('logout/', views.lout, name='logout'),
    path('delete/<pk>', views.delete, name='delete'),
    path('update/<pk>', views.updates, name='updt'),
    path('view/<pk>', views.viePage, name='views'),
    # Resete the password systeam
     path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name='reset_password.html')
         , name='reset_password'),
    path('reset_password_send/', 
         auth_views.PasswordResetDoneView.as_view(template_name='reset_password_send.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), 
         name='password_reset_complete'),

]
