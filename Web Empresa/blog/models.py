from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name="Modificado")

    class META: 
        vervose_name = "categoría"
        vervose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
      return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    content = models.TextField( verbose_name='Contenido')
    published = models.DateField(verbose_name="Fecha de publicación", default=timezone.now())
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True,verbose_name="Modificado")

    class META: 
        vervose_name = "categoría"
        vervose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
      return self.title