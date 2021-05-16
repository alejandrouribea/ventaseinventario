from django.contrib import admin
from gestionInventario.models import Productos

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display= ("id", "nombre", "existencia")
    search_fields= ("id", "nombre")

# Register your models here.
admin.site.register(Productos, ProductosAdmin)