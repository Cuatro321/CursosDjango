# cursos/views.py

from django.views.generic import ListView, DetailView
from .models import Curso

class CursoListView(ListView):
    model = Curso
    template_name       = 'cursos/curso_list.html'
    context_object_name = 'cursos'
    # Ordenar por el campo real de tu modelo: fecha_creado
    queryset = Curso.objects.filter(publicado=True) \
                              .order_by('fecha_creado')

class CursoDetailView(DetailView):
    model               = Curso
    template_name       = 'cursos/curso_detalle.html'
    context_object_name = 'curso'
