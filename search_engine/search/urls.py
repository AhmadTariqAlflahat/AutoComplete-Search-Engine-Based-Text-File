from django.urls import path, include
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('upload/', views.upload, name='upload'),
]
