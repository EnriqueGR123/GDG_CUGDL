from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.show_task, name='task'),
    path('logout/', views.signout, name='signuot'),
    path('signin/', views.signin, name='signin'),
    path('create_task/', views.create_task, name='create_task'),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task_detail/<int:task_id>/complete', views.task_complete, name='task_complete'),
    path('task_detail/<int:task_id>/task_delete', views.task_delete, name='task_delete'),



]
