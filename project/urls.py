from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('speedway.urls')),  # Inclui todas as rotas do app 'speedway'
]
