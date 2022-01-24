from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Todo


def todos(request):
    return render(request, 'todo/todos.html')


@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')

    if title:
        todo = Todo.objects.create(title=title)

    return render(request, 'todo/partials.todo.html', {'todo': todo})