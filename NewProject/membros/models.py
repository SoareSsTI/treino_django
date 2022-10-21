from django.db import models

class Membros(models.Model):
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
