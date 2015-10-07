from django.contrib import admin
from demo.apps.reserva.models import cliente,producto,reserva

#Registro modelos
admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(reserva)
#admin.site.register(fijar_fecha)
