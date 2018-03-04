from django.contrib import admin
from .models import Person, Documento, Venda, Produto


admin.site.register(Person)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
