from django.contrib import admin
from django.urls import path, include
from aplicativo.urls import urlpatterns
from aplicativo import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('registrar/', views.registrar, name='registrar'),
    path('', include(urlpatterns))
]
