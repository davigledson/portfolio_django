from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome", blank=True, null=True)
    tagline = models.CharField(max_length=200, verbose_name="Título", blank=True, null=True)
    bio = models.TextField(verbose_name="Biografia", blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/', verbose_name="Imagem de Perfil", blank=True, null=True)
    github_url = models.URLField(verbose_name="Link do GitHub", blank=True, null=True)
    resume_url = models.URLField(verbose_name="Link do Currículo", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sobre Mim"
        verbose_name_plural = "Sobre Mim"


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Habilidade", blank=True, null=True)
    icon_class = models.CharField(max_length=50, verbose_name="Classe do Ícone (FontAwesome)", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Habilidade Técnica"
        verbose_name_plural = "Habilidades Técnicas"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título do Projeto", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição do Projeto", blank=True, null=True)
    image = models.ImageField(upload_to='project/images/', verbose_name="Imagem do Projeto", blank=True, null=True)
    project_url = models.URLField(verbose_name="Link do Projeto", blank=True, null=True)
    github_url = models.URLField(verbose_name="Link do GitHub", blank=True, null=True)
    skills = models.ManyToManyField(Skill, verbose_name="Habilidades Utilizadas", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"


class Icone(models.Model):
    nome = models.CharField(
        max_length=50,
        unique=True,
        help_text="Nome do ícone do Font Awesome (ex: fab fa-python)"
    )
    tamanho = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="Tamanho do ícone (ex: fa-3x)"
    )

    def __str__(self):
        return f"{self.nome} {self.tamanho}" if self.tamanho else self.nome


class Testimonial(models.Model):
    icone = models.ForeignKey(
        Icone,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Ícone associado ao depoimento"
    )
    name = models.CharField(
        max_length=100,
        help_text="Nome do projeto ou título do depoimento"
    )
    description = models.TextField(
        help_text="Descrição detalhada do projeto ou depoimento"
    )
    technologies = models.CharField(
        max_length=200,
        help_text="Tecnologias usadas (ex: Python, PyAutoGUI, PyQT, Pandas)"
    )
    project_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Link para o projeto (ex: GitHub)"
    )

    def __str__(self):
        return self.name


class StyleConfig(models.Model):
    theme_name = models.CharField(max_length=100, verbose_name="Nome do Tema", blank=True, null=True)
    css_file = models.FileField(upload_to='css/', verbose_name="Arquivo CSS", blank=True, null=True)

    def __str__(self):
        return self.theme_name

    class Meta:
        verbose_name = "Configuração de Estilo"
        verbose_name_plural = "Configurações de Estilo"


class PredefinicaoGeral(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Predefinição", blank=True, null=True)
    objetivo = models.CharField(
        max_length=100,
        verbose_name="Objetivo (Ex: Vaga Python, Vaga PHP)",
        blank=True,
        null=True
    )
    tema_css = models.ForeignKey(
        StyleConfig,
        on_delete=models.SET_NULL,
        verbose_name="Tema CSS",
        blank=True,
        null=True
    )
    sobre_mim = models.ForeignKey(
        AboutMe,
        on_delete=models.SET_NULL,
        verbose_name="Sobre Mim",
        blank=True,
        null=True
    )
    habilidades = models.ManyToManyField(
        Skill,
        verbose_name="Habilidades Destacadas",
        blank=True
    )
    projetos = models.ManyToManyField(
        Project,
        verbose_name="Projetos Destacados",
        blank=True
    )
    depoimentos = models.ManyToManyField(
        Testimonial,
        verbose_name="Depoimentos Destacados",
        blank=True
    )

    def __str__(self):
        return self.nome or f"Predefinição {self.id}"

    class Meta:
        verbose_name = "Predefinição Geral"
        verbose_name_plural = "Predefinições Gerais"