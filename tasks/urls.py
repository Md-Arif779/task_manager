from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteConfirmView,
    TaskDeleteView,
    TaskCreateView
)
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteConfirmView.as_view(), name='task_delete_confirm'),
    path('tasks/<int:pk>/delete/confirmed/', TaskDeleteView.as_view(), name='task_delete'),

    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]





