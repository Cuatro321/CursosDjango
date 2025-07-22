# CursosDjango/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contenido import views as contenido_views
from django.contrib.auth import views as auth_views
from usuarios import views as usuarios_views

urlpatterns = [
    # Redirige a vista personalizada de admin según tipo de usuario
    path('admin/', usuarios_views.admin_personalizado_view, name="admin_personalizado"),

    # Acceso real al admin completo (solo superusuarios son redirigidos)
    path('admin_full/', admin.site.urls),

    # Sitio principal
    path('', contenido_views.mprincipal, name="Principal"),
    path('cursos/', include('cursos.urls', namespace='cursos')),
    path('contacto/', contenido_views.contacto, name="Contacto"),

    # Autenticación
    path('accounts/login/',    auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('accounts/logout/',   auth_views.LogoutView.as_view(next_page='Principal'), name='logout'),
    path('accounts/register/', usuarios_views.RegistroView.as_view(), name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
