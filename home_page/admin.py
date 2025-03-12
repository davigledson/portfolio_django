from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AboutMe, Skill, Project, Icone, Testimonial, StyleConfig, PredefinicaoGeral

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    search_fields = ('name', 'tagline')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_url')
    search_fields = ('title',)
    filter_horizontal = ('skills',)  # Para seleção múltipla de habilidades

@admin.register(Icone)
class IconeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tamanho')
    search_fields = ('nome',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'technologies')
    search_fields = ('name',)

@admin.register(StyleConfig)
class StyleConfigAdmin(admin.ModelAdmin):
    list_display = ('theme_name',)
    search_fields = ('theme_name',)

@admin.register(PredefinicaoGeral)
class PredefinicaoGeralAdmin(admin.ModelAdmin):
    list_display = ('nome', 'objetivo')
    search_fields = ('nome', 'objetivo')
    filter_horizontal = ('habilidades', 'projetos', 'depoimentos')  # Para seleção múltipla