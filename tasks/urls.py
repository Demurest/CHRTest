from django.urls import path 
from .views import list_tasks,buscarJurisprudencias
urlpatterns = [
    path('',list_tasks),
    path('new/',buscarJurisprudencias)
]