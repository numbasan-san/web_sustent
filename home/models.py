
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from rest_framework.fields import Field
from wagtail import blocks
from .body_block import BodyBlock

class HomePage(Page):
    summary = models.CharField(max_length = 140, default = '')
    body = RichTextField(blank = True)
    mary = RichTextField(blank = True)
    corp = RichTextField(blank = True)
    zelda = RichTextField(blank = True)

    content_panels = Page.content_panels + [
        FieldPanel('summary', classname = 'full'),
        FieldPanel('body', classname = 'full'),
        FieldPanel('mary', classname = 'full'),
        FieldPanel('corp', classname = 'full'),
        FieldPanel('zelda', classname = 'full')
    ]

class Login(Page):
    template = 'home/login.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    corp = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('corp', classname = 'full'),
        FieldPanel('body', classname = 'full')
    ]

class Indicadores(Page):
    template = 'home/indicadores.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    corp = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('corp', classname = 'full'),
        FieldPanel('body', classname = 'full')
    ]

    subpage_types = ['NuevoInforme']

class Informes(Page):
    template = 'home/informes.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body', classname = 'full')
    ]


class PMO(Page):
    template = 'home/pmo.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body', classname = 'full')
    ]

class NuevoInforme(Page):
    template = 'home/indicador.html'

    tema_material = models.CharField(max_length = 140, default = '')
    id_indicador = models.CharField(max_length = 140, blank = False)
    medida = models.CharField(max_length = 140, blank = False)
    responsable = models.CharField(max_length = 140, blank = False)
    comentario = models.CharField(max_length = 500, blank = True)
    estado = models.CharField(max_length = 140, blank = False)
    tipo = models.CharField(max_length = 140, blank = False)
    # tipo = RichTextField(blank = False, default = '')
    
    '''
    parametros = StreamField([
        # ('heading', blocks.CharBlock(form_classname="title")),
        ('nombre', blocks.RichTextBlock()),
        ('valor', blocks.RichTextBlock()),
        ('tipo', blocks.RichTextBlock()),
    ], use_json_field=True)
    '''

    content_panels = Page.content_panels + [
        FieldPanel('tema_material', classname = 'full'),
        FieldPanel('id_indicador', classname = 'full'),
        FieldPanel('medida', classname = 'full'),
        FieldPanel('responsable', classname = 'full'),
        FieldPanel('comentario', classname = 'full'),
        FieldPanel('estado', classname = 'full'),
        FieldPanel('tipo', classname = 'full'),
        # FieldPanel('parametros', classname = 'full'),
    ]

    parent_page_types = ['Indicadores']
