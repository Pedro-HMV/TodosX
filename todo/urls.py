from django.urls import path
from .views import add_todo, todos

urlpatterns = [
    path('', todos, name='todos'),
    path('add-todo/', add_todo, name='add-todo')
]
