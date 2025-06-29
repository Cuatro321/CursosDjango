# cursos/urls.py

from django.urls import path
from .views import CursoListView, CursoDetailView

app_name = 'cursos'

urlpatterns = [
    # Listado en /cursos/
    path('',        CursoListView.as_view(),   name='lista'),
    # Detalle en /cursos/<pk>/
    path('<int:pk>/', CursoDetailView.as_view(), name='detalle'),
]
