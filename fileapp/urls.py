"""
URL configuration for fileprjct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('adminlogin', views.adminlogin, name="adminlogin"),
    path('adminhome', views.adminhome, name="adminhome"),
    path('user_register', views.user_register, name="user_register"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('userhome', views.userhome, name="userhome"),
    path('logout', views.logout, name="logout"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('feedback', views.feedback, name="feedback"),
    path('view_feedback', views.view_feedback, name="view_feedback"),
    path('delete_feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('view_users', views.view_users, name='view_users'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('my_files', views.my_files, name='my_files'),
    path('update_file/<int:file_id>/', views.update_file, name='update_file'),

    path('view_all_files', views.view_all_files, name='view_all_files'),
    path('send_request/<int:file_id>/', views.send_request, name='send_request'),
    path('view_requests', views.view_requests, name='view_requests'),
    path('approve_request/<int:req_id>/', views.approve_request, name='approve_request'),
    path('reject_request/<int:req_id>/', views.reject_request, name='reject_request'),
    path('delete_request/<int:req_id>/', views.delete_request, name='delete_request'),
    path('my_approved_files', views.my_approved_files, name='my_approved_files'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),

    path('admin_view_files', views.admin_view_files, name='admin_view_files'),
    path('delete_uploaded_file/<int:file_id>/', views.delete_uploaded_file, name='delete_uploaded_file'),
]
