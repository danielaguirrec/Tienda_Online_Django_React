from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion","tfno","email")
    search_fields=("nombre","direccion")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("precio",)


# Register your models here.
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
