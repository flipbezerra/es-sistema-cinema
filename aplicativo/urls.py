from django.conf.urls.static import static
from aplicativo.views import index, index_auth, filmes, filme_list, cartaz, assento
from django.urls import path
from GerenciaCinema import settings

app_name = 'aplicativo'

urlpatterns = [
    path('', index),
    path('index_auth', index_auth, name='index_auth'),
    path('filmes', filmes, name='filmes'),
    path('filmes_cartaz', filme_list, name='filmes_cartaz'),
    path('cartaz', cartaz, name='cartaz'),
    path('assento', assento, name='assento'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)