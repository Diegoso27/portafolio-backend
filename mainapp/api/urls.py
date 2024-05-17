from django.urls import path

from mainapp.api.views import registrar_propiedad


urlpatterns = [
    path('registrar-propiedad/', registrar_propiedad, name='registrar-propiedad'),
]