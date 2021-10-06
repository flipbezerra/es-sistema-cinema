from django.db import models
from stdimage import StdImageField


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=32)
    sobrenome = models.CharField('Sobrenome', max_length=32)
    email = models.EmailField('Email', max_length=32)

    def __str__(self):
        return "{}".format(self.nome)


class Assentos(models.Model):
    registro = models.CharField('Sigla', max_length=4)
    livre = models.BooleanField(default=True)

    def __str__(self):
        return "{} | Livre ={}".format(self.registro, self.livre)

class Cartaz(models.Model):
    dataCartaz = models.DateTimeField(verbose_name='Data do Cartaz')
    assentos = models.ManyToManyField(Assentos)

    def __str__(self):
        return "Dia {} ás {}".format(self.dataCartaz.strftime('%d/%m/%Y'), self.dataCartaz.strftime('%H:%M'))

class Filme(models.Model):
    CATEGORIA_CHOICES = (
        ('Action', 'Ação'), ('Adventure', 'Aventura'), ('Comedy', 'Comédia'), ('Terror', 'Terror'), ('Drama', 'Drama'),
        ('Fantasy', 'Fantasia'), ('Sci-Fi', 'Ficção'), ('Romance', 'Romance')
    )

    CLASSIFICACAO_CHOICES = (
        ('Livre', 'Livre'), ('10', '10+'), ('12', '12+'), ('14', '14+'),
        ('16', '16+'), ('18', '18+')
    )

    cartaz = models.OneToOneField(Cartaz, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=16)
    sinopse = models.CharField('Sinopse', max_length=128)
    categoria = models.CharField(max_length=32, choices=CATEGORIA_CHOICES)
    classificacao = models.CharField(max_length=32, choices=CLASSIFICACAO_CHOICES)
    duracao = models.CharField('Duração', max_length=16)
    capa = StdImageField('Capa do Filme', upload_to='imagens', variations={'thumb': (90, 90)})

    def __str__(self):
        return "{}".format(self.nome)


class Recibo(models.Model):
    assento = models.IntegerField()
    preco = models.DecimalField(max_digits=16, decimal_places=2)

