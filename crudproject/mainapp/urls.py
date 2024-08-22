from django.contrib import admin
from django.urls import path
from .views import index
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('det/<int:id>/', views.detailsView, name='detail'),
    path('add/', views.addView, name='add'), 
    path('upd/<int:id>/', views.updateView, name='update'),
    path('del/<int:id>/', views.deleteView, name='delete'),
]