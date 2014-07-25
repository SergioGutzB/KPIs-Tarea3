from django.contrib import admin
from indicadores.models import *
# Register your models here.
class IndicadorAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','valor')

admin.site.register(Indicador, IndicadorAdmin) 