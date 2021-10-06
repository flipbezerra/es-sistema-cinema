from django.conf.urls.static import static
from aplicativo.views import index, index_auth, filmes, cliente, filme_list, cartaz, assento
from django.urls import path
from GerenciaCinema import settings

app_name = 'aplicativo'

urlpatterns = [
    path('', index),
    path('index_auth', index_auth, name='index_auth'),
    path('filmes', filmes, name='filmes'),
    path('cliente', cliente, name='cliente'),
    path('filme_list', filme_list, name='filme_list'),
    path('cartaz', cartaz, name='cartaz'),
    path('assento', assento, name='assento'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)