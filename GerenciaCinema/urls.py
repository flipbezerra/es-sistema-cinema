from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from aplicativo.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
