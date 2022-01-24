from django.urls import path
from .views import add_todo, todos, update_todo

urlpatterns = [
    path('', todos, name='todos'),
    path('add-todo/', add_todo, name='add-todo'),
    path('update/<int:pk>/', update_todo, name='update-todo')
]
