from django.urls import path
from Track import views

urlpatterns = [
     path('register/', views.register, name = 'register'),
     path('<int:new_id>/', views.all_Track, name='all_Track'),
      path('', views.all_Track, name='all_Track'),
      
]