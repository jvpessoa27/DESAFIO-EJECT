from django.contrib import admin

from desafio2.models import Inicio
from .models import Formulario, Inicio
from .models import SegundaParte
from .models import Conhecer
from .models import Portfolio
# Register your models here.
class InicioAdmin(admin.ModelAdmin):
    list_display1 = ('id', 'titulo')

admin.site.register(Inicio, InicioAdmin)
admin.site.register(SegundaParte)
admin.site.register(Conhecer)
admin.site.register(Portfolio)
admin.site.register(Formulario )
