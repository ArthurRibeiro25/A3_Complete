from django.db import models
from aviao.models import AvioesClass
from passageiro.models import PassageirosClass

# Create your models here.

class PassagensClass(models.Model):
    nome = models.ForeignKey(PassageirosClass, on_delete=models.CASCADE)
    destino = models.ForeignKey(AvioesClass, on_delete=models.CASCADE)
    assento = models.CharField('Assento', max_length=5)
    horario = models.CharField('Horario', max_length=5)
    portao = models.CharField('Portao', max_length=3)
    
    class Meta:
        verbose_name = 'Passagem'
        verbose_name_plural = 'Passagens'
        ordering =['id']

    def __str__(self):
        return self.assento