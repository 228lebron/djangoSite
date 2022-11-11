from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update_competitors/', views.update, name='update_competitors'),
]