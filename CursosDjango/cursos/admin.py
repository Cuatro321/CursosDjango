from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return super().get_model_perms(request)

    # Campos a mostrar en la lista de objetos
    list_display = (
        'titulo',
        'nivel',
        'precio',
        'publicado',
        'fecha_creado',
    )
    # Búsqueda por texto
    search_fields = ('titulo', 'descripcion')

    # Filtros laterales
    list_filter = ('nivel', 'publicado', 'fecha_creado')

    # Filtros por fecha (barra superior)
    date_hierarchy = 'fecha_creado'

    # Campos de solo lectura
    readonly_fields = ('fecha_creado',)

    # Reordenar campos y renombrar etiquetas en el formulario
    fieldsets = (
        (None, {
            'fields': (
                ('titulo', 'nivel'),
                'descripcion',
                ('precio', 'duracion', 'publicado'),
                'imagen',
            ),
            'description': 'Registro de un nuevo curso',
        }),
        ('Metadatos', {
            'fields': ('fecha_creado',),
            'classes': ('collapse',),
        }),
    )

    # Orden por fecha de creación (de más antiguo a más reciente)
    ordering = ('fecha_creado',)
admin.site.site_header = 'CONVOCATORIAS'
admin.site.index_title = 'Cursos'
admin.site.site_title = 'Gestión de Convocatorias'