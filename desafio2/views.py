from imghdr import what
from multiprocessing import context
from django.shortcuts import render

from desafio2.models import Inicio
from desafio2.models import SegundaParte
from desafio2.models import Conhecer
from desafio2.models import Portfolio
from desafio2.models import Formulario
# Create your views here.

def home(request):
    inicio = Inicio.objects.last()
    segundaparte = SegundaParte.objects.last()
    conhecer = Conhecer.objects.last()
    portfolio = Portfolio.objects.last()
    formulario = Formulario.objects.last()

    context = {
        'inicio': inicio,
        'segundaparte': segundaparte,
        'conhecer': conhecer,
        'portfolio': portfolio,
        'formulario': formulario

    }

    if request.method == 'POST':
        email = request.POST['email']

        form = Formulario(email=email)
        form.save()

    return render(request, 'index.html', context)