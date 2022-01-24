from django.urls import path
from .views import todos

urlpatterns = [
    path('', todos, name='todos')
]
