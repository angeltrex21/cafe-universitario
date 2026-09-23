
from django.contrib import admin

from .models import MensajeContacto


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'correo',
        'asunto',
        'fecha'
    )

    search_fields = (
        'nombre',
        'correo',
        'asunto'
    )

    list_filter = (
        'fecha',
    )

    readonly_fields = (
        'fecha',
    )   