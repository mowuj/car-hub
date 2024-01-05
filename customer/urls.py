from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.UserLoginView.as_view(), name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_pass/', views.change_pass, name='change_pass'),
    
]
