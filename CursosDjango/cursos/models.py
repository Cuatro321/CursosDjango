from django.db import models
from ckeditor.fields import RichTextField

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
    imagen       = models.ImageField("Imagen del curso", upload_to='cursos/', null=True, blank=True)

    class Meta:
        ordering = ['fecha_creado']
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.titulo


class Actividad(models.Model):
    curso   = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment  = RichTextField(verbose_name="Descripción de Actividad")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):
       
        return self.coment[:30] + '…'
