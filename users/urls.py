from django.contrib import admin
from django.urls import path
from .views import RegisterView
from .views import LostView
from .views import FoundView,LostListView,FoundListView

from rest_framework_simplejwt.views import (TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/' , TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('lost/', LostView.as_view()),
    path('found/', FoundView.as_view()),
    path('lostlist/',LostListView.as_view()),
    path('Foundlist/',FoundListView.as_view()),

    ]