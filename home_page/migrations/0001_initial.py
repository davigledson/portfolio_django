# Generated by Django 4.2.20 on 2025-03-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('tagline', models.CharField(max_length=200, verbose_name='Título')),
                ('bio', models.TextField(verbose_name='Biografia')),
                ('profile_image', models.ImageField(upload_to='images/', verbose_name='Imagem de Perfil')),
                ('github_url', models.URLField(verbose_name='Link do GitHub')),
                ('resume_url', models.URLField(verbose_name='Link do Currículo')),
            ],
            options={
                'verbose_name': 'Sobre Mim',
                'verbose_name_plural': 'Sobre Mim',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome da Habilidade')),
                ('icon_class', models.CharField(max_length=50, verbose_name='Classe do Ícone (FontAwesome)')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Habilidade Técnica',
                'verbose_name_plural': 'Habilidades Técnicas',
            },
        ),
        migrations.CreateModel(
            name='StyleConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=100, verbose_name='Nome do Tema')),
                ('css_file', models.FileField(upload_to='css/', verbose_name='Arquivo CSS')),
            ],
            options={
                'verbose_name': 'Configuração de Estilo',
                'verbose_name_plural': 'Configurações de Estilo',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(verbose_name='Citação')),
                ('source_name', models.CharField(max_length=100, verbose_name='Nome da Fonte')),
                ('source_info', models.CharField(max_length=200, verbose_name='Informação da Fonte')),
                ('icon_class', models.CharField(max_length=50, verbose_name='Classe do Ícone (FontAwesome)')),
                ('project_url', models.URLField(blank=True, null=True, verbose_name='Link do Projeto')),
            ],
            options={
                'verbose_name': 'Depoimento',
                'verbose_name_plural': 'Depoimentos',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título do Projeto')),
                ('description', models.TextField(verbose_name='Descrição do Projeto')),
                ('image', models.ImageField(upload_to='project/images/', verbose_name='Imagem do Projeto')),
                ('project_url', models.URLField(verbose_name='Link do Projeto')),
                ('github_url', models.URLField(blank=True, null=True, verbose_name='Link do GitHub')),
                ('skills', models.ManyToManyField(to='home_page.skill', verbose_name='Habilidades Utilizadas')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
    ]
