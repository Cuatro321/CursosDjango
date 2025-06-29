from django.shortcuts import render, redirect
from django.contrib import messages

def mprincipal(request):
    return render(request, 'contenido/principal.html')

def cursos(request):
 
    return render(request, 'contenido/cursos.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip()
        asunto = request.POST.get('asunto', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()
        if nombre and correo and mensaje:
       
            messages.success(request, f'Gracias, {nombre}. Tu mensaje ha sido enviado.')
            return redirect('Contacto')
        else:
            messages.error(request, 'Por favor completa los campos obligatorios.')
    return render(request, 'contenido/contacto.html')
