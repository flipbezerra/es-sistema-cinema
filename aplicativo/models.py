from django.db import models
from django.urls import reverse
#from stdimage import StdImageField

# Create your models here.
class AdminSide(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=16)

class MovieMaster(models.Model):
    m_name = models.CharField('Nome', max_length=50)
    m_desc = models.CharField('Sinopse', max_length=128)
    m_image = models.ImageField('Capa do Filme', upload_to="pics/")

    class Meta:
        unique_together = ["m_name", "m_desc", "m_image",]

    def get_absolute_url(self):
        return reverse("setadmin:addmovie")

    def str(self):
        return self.m_name

class SetMovie(models.Model):
    active = models.ForeignKey(MovieMaster, on_delete=models.CASCADE)
    show = models.CharField('Sessão', max_length=50)
    start_time = models.DateField()
    end_time = models.DateField()
    price = models.IntegerField()
    seats = models.CharField(max_length=100, default="")

    class Meta:
        unique_together = ["active", "show", "start_time", "end_time"]

    def get_absolute_url(self):
        return reverse("setadmin:setmovie")
    
#class Filme(models.Model):
#    CLASSIFICACAO_CHOICES = (
#        ('Livre', 'Livre'), ('10', '10+'), ('12', '12+'), ('14', '14+'),
#        ('16', '16+'), ('18', '18+')
#    )
#    
#    nome = models.CharField('Nome', max_length=16)
#    sinopse = models.CharField('Sinopse', max_length=128)
#    classificacao = models.CharField(max_length=32, choices=CLASSIFICACAO_CHOICES)
#    duracao = models.CharField('Duração', max_length=16)
#    capa = StdImageField('Capa do Filme', upload_to='imagens', variations={'thumb': (90, 90)})
#
#    def __str__(self):
#        return "{}".format(self.nome)