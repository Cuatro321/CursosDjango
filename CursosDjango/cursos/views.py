from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from .models import Curso
from .forms import CursoForm

class CursoListView(ListView):
    model               = Curso
    template_name       = 'cursos/curso_list.html'
    context_object_name = 'cursos'
    queryset = Curso.objects.filter(publicado=True) \
                              .order_by('fecha_creado')
    paginate_by = 9  # opcional

class CursoDetailView(DetailView):
    model               = Curso
    template_name       = 'cursos/curso_detalle.html'
    context_object_name = 'curso'

class CursoCreateView(CreateView):
    model         = Curso
    form_class    = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url   = reverse_lazy('cursos:lista')

class CursoUpdateView(UpdateView):
    model         = Curso
    form_class    = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url   = reverse_lazy('cursos:lista')

class CursoDeleteView(DeleteView):
    model         = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url   = reverse_lazy('cursos:lista')
