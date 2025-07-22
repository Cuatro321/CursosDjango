# cursos/urls.py
from django.urls import path
from .views import (
    CursoListView, CursoDetailView,
    CursoCreateView, CursoUpdateView, CursoDeleteView
)

app_name = 'cursos'
urlpatterns = [
    path('',                CursoListView.as_view(),   name='lista'),
    path('nuevo/',          CursoCreateView.as_view(), name='nuevo'),
    path('<int:pk>/',       CursoDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/',CursoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', CursoDeleteView.as_view(), name='eliminar'),
]
