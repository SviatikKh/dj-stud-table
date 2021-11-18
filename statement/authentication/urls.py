from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.all_users, name='users_list'),
    path('<int:id>/', views.get_by_id, name='get_user'),
    path('create/', UserCreate.as_view(), name='create'),
    path('delete/<int:id>/', views.delete_user_by_id, name='delete_user'),
    path('clean/', views.delete_all_users, name='delete_all_users'),
    path('register/', views.register, name='register'),
    path('rest_create/', UserCreateView.as_view()),
    path('rest_all/', UsersListView.as_view()),
    path('rest_detail/<int:pk>/', UserDetailView.as_view()),

]