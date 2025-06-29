from django.db import models

class Curso(models.Model):
    titulo       = models.CharField("Título", max_length=200)
    descripcion  = models.TextField("Descripción")
    precio       = models.DecimalField("Precio (USD)", max_digits=6, decimal_places=2)
    duracion     = models.PositiveIntegerField("Duración (horas)")
    nivel        = models.CharField(
        "Nivel",
        max_length=10,
        choices=[
            ('INIC', 'Principiante'),
            ('INT', 'Intermedio'),
            ('ADV', 'Avanzado'),
        ],
        default='INIC'
    )
    publicado    = models.BooleanField("Publicado", default=False)
    fecha_creado = models.DateTimeField("Fecha de creación", auto_now_add=True)
    imagen       = models.ImageField(
        "Imagen del curso",
        upload_to='cursos/',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['fecha_creado']  # de más antigua a más reciente
        verbose_name = "Convocatoria"
        verbose_name_plural = "Convocatorias"

    def __str__(self):
        return self.titulo