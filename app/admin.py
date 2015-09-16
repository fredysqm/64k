from django.contrib import admin
from app.models import slink, opcion

class slink_admin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'url', 'clicks','acceso')
    search_fiels = ('id', 'slug',)
    ordering = ['-id']

class opcion_admin(admin.ModelAdmin):
    list_display = ('clave', 'valor',)
    list_editable = ('valor',)

admin.site.register(slink, slink_admin)
admin.site.register(opcion, opcion_admin)
