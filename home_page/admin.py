from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AboutMe, Skill, Project, Testimonial, StyleConfig, PredefinicaoGeral


admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(StyleConfig)
@admin.register(PredefinicaoGeral)
class PredefinicaoGeralAdmin(admin.ModelAdmin):
    list_display = ('nome', 'objetivo')
    filter_horizontal = ('habilidades', 'projetos', 'depoimentos')