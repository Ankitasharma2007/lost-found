from django.urls import path
from Track import views
from . views import register_echo


urlpatterns = [
     path('register/', views.register, name = 'register'),
     path('<int:new_id>/', views.all_Track, name='all_Track'),
     path('', views.all_Track, name='all_Track'),
     path('echo', register_echo, name='register'),
]