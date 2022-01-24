from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('todo.urls')),
    path('admin/', admin.site.urls),
]
