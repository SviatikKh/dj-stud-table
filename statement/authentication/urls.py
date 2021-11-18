from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.all_users, name='users_list'),
    path('<int:id>/', views.get_by_id, name='get_user'),
    path('create_user/', UserCreate.as_view(), name='create_user'),
    path('delete/<int:id>/', views.delete_user_by_id, name='delete_user'),
    path('clean/', views.delete_all_users, name='delete_all_users'),
    path('register_user/', views.register, name='register_user'),
    path('rest_create_user/', UserCreateView.as_view()),
    path('rest_all_users/', UsersListView.as_view()),
    path('rest_detail_user/<int:pk>/', UserDetailView.as_view()),

]