from django.db import models

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Publico(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Curso(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    descricao = models.TextField('Descrição')
    vagas = models.IntegerField('Vagas')
    carga_horaria = models.IntegerField('Carga Horária')
    data = models.DateField('Data')
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publico = models.ManyToManyField(Publico)



'''
Estamos trabalhando com ORM (Object Relational Mapping) do Django, que é uma forma de mapear objetos Python para tabelas em um banco de dados relacional.
- Modelar o banco de dados é criar classes que representam as tabelas do banco de dados.
'''
# Create your models here.
