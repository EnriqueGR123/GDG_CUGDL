from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.show_task, name='task'),
    path('logout/', views.signout, name='signuot'),
    path('signin/', views.signin, name='signin'),
    path('create_task/', views.create_task, name='create_task')
]
