from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Inicio(models.Model):
    image = models.ImageField(verbose_name = 'Imagem da logo', upload_to = 'fotos', default = '')
    titulo1 = models.CharField(verbose_name = 'Titulo inicial parte 1', max_length = 250)
    descricao1 = models.TextField(verbose_name = 'Mensagem de efeito parte 1', max_length = 500, default = '')
    text_button1 = models.CharField(verbose_name = 'Texto-Botão 1', max_length = 100, default = '')
    text_button2 = models.CharField(verbose_name = 'Texto-Botão 2', max_length = 100, default = '')

def __str__(self):
    return f'{self.titulo1}'

class SegundaParte(models.Model):
    tituloprincipal = models.CharField(verbose_name = 'Titulo principal', max_length = 250, default = '')
    titulo1 = models.CharField(verbose_name = 'Titulo 1', max_length = 250, default = '')
    descricao1 = models.TextField(verbose_name = 'Descrição de Quem Somos parte 1', max_length = 250, default = '')
    titulo2 = models.CharField(verbose_name = 'Titulo 2', max_length = 250, default = '')
    descricao2 = models.TextField(verbose_name = 'Descrição de Quem Somos parte 2', max_length = 250, default = '')
    titulo3 = models.CharField(verbose_name = 'Titulo 3', max_length = 250, default = '')
    descricao3 = models.TextField(verbose_name = 'Descrição de Quem Somos parte 3', max_length = 250, default = '')
    titulo4 = models.CharField(verbose_name = 'Titulo 4', max_length = 250, default = '')
    descricao4 = models.TextField(verbose_name = 'Descrição de Quem Somos parte 4', max_length = 250, default = '')
    titulo5 = models.CharField(verbose_name = 'Titulo 5', max_length = 250, default = '')
    descricao5 = models.TextField(verbose_name = 'Descrição de Quem Somos parte 5', max_length = 250, default = '')
    titulo6 = models.CharField(verbose_name = 'Titulo 6', max_length = 250, default = '')
    descricao6 = models.TextField(verbose_name = 'Descrição de Quem Somos parte 6', max_length = 250, default = '')

    def __str__(self):
        return f'{self.tituloprincipal}'

class Conhecer(models.Model):
    titulo = models.CharField(verbose_name = 'Titulo de Serviços', max_length = 250)
    descricao = models.TextField(verbose_name = 'Descrição', max_length = 250, default = '')
    video = models.CharField(verbose_name = 'Video', max_length = 300)

    def __str__(self):
        return f'{self.titulo}'

class Portfolio(models.Model):
    titulo = models.CharField(verbose_name = 'Titulo', max_length = 250, default = '')
    descricao = models.TextField(verbose_name = 'Descrição', max_length = 250, default = '')
    text_button = models.CharField(verbose_name = 'Texto-Botão', max_length = 100, default = '')

    def __str__(self):
        return f'{self.titulo}'

class Formulario(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'
