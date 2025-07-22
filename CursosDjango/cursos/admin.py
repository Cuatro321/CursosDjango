from django.contrib import admin
from .models import Curso, Actividad

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display    = ('titulo','nivel','precio','publicado','fecha_creado')
    search_fields   = ('titulo','descripcion')
    list_filter     = ('nivel','publicado','fecha_creado')
    date_hierarchy  = 'fecha_creado'
    readonly_fields = ('fecha_creado',)
    fieldsets = (
        (None, {
            'fields': (
                ('titulo','nivel'),
                'descripcion',
                ('precio','duracion','publicado'),
                'imagen',
            ),
            'description': 'Registro de un nuevo curso',
        }),
        ('Metadatos', {
            'fields': ('fecha_creado',),
            'classes': ('collapse',),
        }),
    )
    ordering = ('fecha_creado',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display    = ('curso','created')
    search_fields   = ('coment',)
    date_hierarchy  = 'created'
    readonly_fields = ('created',)
    
# Personalización global del admin
admin.site.site_header  = 'CONVOCATORIAS'
admin.site.index_title  = 'Cursos'
admin.site.site_title   = 'Gestión de Convocatorias'

