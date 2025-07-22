# cursos/forms.py
from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model  = Curso
        fields = ['titulo','descripcion','precio','duracion','nivel','publicado','imagen']
