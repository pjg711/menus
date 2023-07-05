from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.


class Menu(TranslatableModel):
    activo = models.BooleanField(default=True, verbose_name="Activo")
    MenuType = models.IntegerField(
        db_index=True,
        verbose_name="Id de menu padre",
        help_text="Indique si es submenu poniendo aca el id del menu padre",
    )
    MenuLink = models.CharField(
        max_length=100, blank=True, verbose_name="Submenu", help_text=""
    )
    MenuURL = models.CharField(
        max_length=100, blank=True, verbose_name="URL django", help_text=""
    )
    orden = models.IntegerField(
        default=0, verbose_name="Orden", help_text="Orden de aparición en la página web"
    )
    pagina_asociada = models.ForeignKey(
        "Pagina",
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        verbose_name="Pagina web asociada",
        help_text="",
    )
    translations = TranslatedFields(
        # Menu padre para traducción
        MenuName1=models.CharField(max_length=100, verbose_name="Menu", help_text=""),
        # Submenu para traducción
        SubmenuName1=models.CharField(
            max_length=100,
            blank=True,
            verbose_name="Nombre del submenu si tiene",
            help_text="",
        ),
    )

    def __str__(self):
        return self.MenuName1

    def __unicode__(self):
        return self.MenuName1

    def get_absolute_url(self):
        return reverse("app:menu", args=[self.MenuLink])

    class Meta:
        app_label = "app"
        db_table = "app_menus"
        verbose_name = "Menú"
        verbose_name_plural = "29. Menús"
        ordering = ["orden"]

class Pagina(TranslatableModel):
    activo = models.BooleanField(default=True)
    titulo = models.CharField(max_length=1000, verbose_name="Titulo")
    slug = models.SlugField(default=None, unique=True, verbose_name="Enlace")
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    translations = TranslatedFields(
        contenido=RichTextField(verbose_name="Contenido", blank=True),
    )

    class Meta:
        app_label = "app"
        verbose_name = "Página web"
        verbose_name_plural = "26. Páginas web"
        ordering = ["created_date"]

    def __str__(self):
        return "activo: " + str(self.activo) + ", titulo: " + self.titulo

    def link_pagina(self):
        try:
            return mark_safe('<a href="/pagina/%s">Link a pagina</a>' % (self.slug))
        except:
            return ""

    def get_absolute_url(self):
        return reverse("pagina-web", kwargs={"pagina": self.slug})

