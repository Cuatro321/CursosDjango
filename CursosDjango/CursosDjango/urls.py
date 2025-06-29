# CursosDjango/urls.py

from django.contrib import admin
from django.urls import path, include     # ← incluimos include
from django.conf import settings
from django.conf.urls.static import static

from contenido import views

urlpatterns = [
    path('admin/',    admin.site.urls),
    path('',          views.mprincipal,    name="Principal"),
    path('cursos/',   include('cursos.urls', namespace='cursos')),  # ← eliminada la línea anterior que apuntaba a views.cursos
    path('contacto/', views.contacto,      name="Contacto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
