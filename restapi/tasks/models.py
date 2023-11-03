from django.db import models

class Task(models.Model):
    FINAL = (
        ('S', 'Sim'),
        ('N', 'Não')
    )
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    completo = models.CharField(max_length=1, choices=FINAL, blank=False, null=False, default='N')

    def __str__(self):
        return self.nome
