from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutMe, Skill, Project, Testimonial, PredefinicaoGeral

from django.shortcuts import render
from .models import PredefinicaoGeral


def index(request):
    # Recupera a primeira predefinição (ou a desejada)
    predefinicao = PredefinicaoGeral.objects.first()

    # Passa a predefinição como parte de um dicionário de contexto
    context = {
        'predefinicao': predefinicao
    }

    return render(request, 'home_page/index.html', context)

def resume(request):
	return render(request, 'home_page/resume.html')