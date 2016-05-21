from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturalday

from app.models import Slink, Opcion



def slink_activar_action(modeladmin, request, queryset):
    queryset.update(estado='A')

def slink_deshabilitar_action(modeladmin, request, queryset):
    queryset.update(estado='D')

slink_activar_action.short_description = "Activar slink(s) seleccionado(s)"
slink_deshabilitar_action.short_description = "Deshabilitar slink(s) seleccionado(s)"

class SlinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'url', 'visitas', 'creado','acceso')
    search_fiels = ('id', 'slug',)
    list_filter = ('estado',)
    ordering = ['-id']
    actions = (slink_activar_action, slink_deshabilitar_action,)

class OpcionAdmin(admin.ModelAdmin):
    list_display = ('clave', 'valor',)
    list_editable = ('valor',)

admin.site.register(Slink, SlinkAdmin)
admin.site.register(Opcion, OpcionAdmin)
