# Generated by Django 3.2.5 on 2023-07-05 13:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=1000, verbose_name='Titulo')),
                ('slug', models.SlugField(default=None, unique=True, verbose_name='Enlace')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Página web',
                'verbose_name_plural': '26. Páginas web',
                'ordering': ['created_date'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('MenuType', models.IntegerField(db_index=True, help_text='Indique si es submenu poniendo aca el id del menu padre', verbose_name='Id de menu padre')),
                ('MenuLink', models.CharField(blank=True, max_length=100, verbose_name='Submenu')),
                ('MenuURL', models.CharField(blank=True, max_length=100, verbose_name='URL django')),
                ('orden', models.IntegerField(default=0, help_text='Orden de aparición en la página web', verbose_name='Orden')),
                ('pagina_asociada', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pagina', verbose_name='Pagina web asociada')),
            ],
            options={
                'verbose_name': 'Menú',
                'verbose_name_plural': '29. Menús',
                'db_table': 'app_menus',
                'ordering': ['orden'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PaginaTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, verbose_name='Contenido')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='app.pagina')),
            ],
            options={
                'verbose_name': 'Página web Translation',
                'db_table': 'app_pagina_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MenuTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('MenuName1', models.CharField(max_length=100, verbose_name='Menu')),
                ('SubmenuName1', models.CharField(blank=True, max_length=100, verbose_name='Nombre del submenu si tiene')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='app.menu')),
            ],
            options={
                'verbose_name': 'Menú Translation',
                'db_table': 'app_menus_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]