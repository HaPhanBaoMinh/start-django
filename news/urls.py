from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addPost, name='addPost'),
    path('save/', views.saveNewPost, name='save')
]