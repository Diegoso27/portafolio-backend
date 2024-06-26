from django.urls import path

from mainapp.api.views import registrar_propiedad, listar_propiedades,datos_user, registrar_infante, listar_infantes, detalle_infante, obtener_servicios, obtener_propiedad


urlpatterns = [
    path('registrar-propiedad/', registrar_propiedad, name='registrar-propiedad'),
    path('listar-propiedades/', listar_propiedades, name='listar-propiedades'),
    path('datos-user/', datos_user, name='datos-user'),
    path('registrar-infante/<int:propiedad_id>/', registrar_infante, name='registrar-infante'),
    path('listar-infantes/<int:propiedad_id>/', listar_infantes, name='listar-infantes'),
    path('detalle-infante/<int:infante_id>/', detalle_infante, name='detalle-infante'),
    path('obtener-servicios/<int:propiedad_id>/', obtener_servicios, name='obtener_servicios'),
    path('obtener-propiedad/<int:propiedad_id>/', obtener_propiedad, name='obtener-propiedad'),

]   