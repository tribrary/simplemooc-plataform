from django.db import models

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descricao', blank=True)
    start_date = models.DateField('Data de inicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem')
    create_at = models.DateTimeField('Atualizado em', auto_now=True)
