from django.shortcuts import loader
from django.http import HttpResponse
from .models import Membros

def index(request):

    membros = Membros.objects.all().values()
    template = loader.get_template('index.html')
    contexto = {
        'membros': membros,
    }
    return HttpResponse(template.render(contexto, request))
