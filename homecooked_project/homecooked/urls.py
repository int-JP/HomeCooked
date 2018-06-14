
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_create, name='profile'),
    path('kitchens', views.kitchen, name='kitchen'),
]