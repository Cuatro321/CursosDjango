from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistroForm

# Vista para el registro de usuarios
class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')


# Vista personalizada para acceso a /admin/
@login_required
def admin_personalizado_view(request):
    if request.user.is_superuser:
        return redirect('/admin_full/')
    else:
        return render(request, 'usuarios/perfil_usuario.html', {'usuario': request.user})
