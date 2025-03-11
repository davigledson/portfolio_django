from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutMe, Skill, Project, Testimonial, PredefinicaoGeral

from django.shortcuts import render
from .models import AboutMe, Skill, Project, Testimonial, PredefinicaoGeral

def index(request):
    # Busca a predefinição geral (ou a primeira, se houver várias)
    predefinicao = PredefinicaoGeral.objects.first()

    # Busca os dados relacionados
    sobre_mim = predefinicao.sobre_mim if predefinicao else None
    habilidades = predefinicao.habilidades.all() if predefinicao else Skill.objects.all()
    projetos = predefinicao.projetos.all() if predefinicao else Project.objects.all()
    depoimentos = predefinicao.depoimentos.all() if predefinicao else Testimonial.objects.all()

    context = {
        'sobre_mim': sobre_mim,
        'habilidades': habilidades,
        'projetos': projetos,
        'depoimentos': depoimentos,
    }

    return render(request, 'home_page/index.html', context)


def resume(request):
	return render(request, 'home_page/resume.html')