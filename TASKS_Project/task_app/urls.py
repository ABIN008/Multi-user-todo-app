from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('register',views.signup,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('userindex',views.userindex,name='userindex'),
    path('taskadd',views.TaskAdd,name='taskadd'),
    path('taskview',views.TaskView,name='taskview'),
    path('assign',views.TaskAssign,name='assign'),
    path('taskedit/<str:pk>/',views.EditTask,name='taskedit'),
    path('taskdelete/<str:pk>/',views.TaskDelete,name='taskdelete'),
]