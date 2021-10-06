from django.contrib import admin
from aplicativo.models import Filme, Cliente, Cartaz, Assentos

# Register your models here.

admin.site.register(Filme)
admin.site.register(Cliente)
admin.site.register(Cartaz)
admin.site.register(Assentos)