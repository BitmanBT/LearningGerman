from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('vocabulary', views.vocabulary, name='vocabulary'),
    path('exercises', views.exercises, name='exercises'),
    path('add_words', views.add_words, name='add_words'),
]
