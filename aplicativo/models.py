from django.db import models
from stdimage import StdImageField

class Filme(models.Model):
    CLASSIFICACAO_CHOICES = (
        ('Livre', 'Livre'), ('10+', '10+'), ('12+', '12+'), ('14+', '14+'),
        ('16+', '16+'), ('18+', '18+')
    )

    nome = models.CharField('Nome', max_length=32)
    sinopse = models.CharField('Sinopse', max_length=128)
    classificacao = models.CharField(max_length=32, choices=CLASSIFICACAO_CHOICES)
    duracao = models.CharField('Duração', max_length=16)
    capa = StdImageField('Capa do Filme', upload_to='imagens', variations={'thumb': (90, 90)})
    trailer = models.CharField('Trailer do filme', max_length=32)

    def __str__(self):
        return "{}".format(self.nome)

class Sessao(models.Model):
    dataCartaz = models.DateTimeField(verbose_name='Data do Cartaz')
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)

    def __str__(self):
        return "Sessão de {}, dia {} ás {}".format(self.filme.nome, self.dataCartaz.strftime('%d/%m/%Y'), self.dataCartaz.strftime('%H:%M'))
    
class Assentos(models.Model):
    ocupado = models.BooleanField(default=False)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.livre == True:
            return "{} | Livre".format(self.sessao.dataCartaz)
        else:
            return "{} | Ocupado".format(self.sessao.dataCartaz)