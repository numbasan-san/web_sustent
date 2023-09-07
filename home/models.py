
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks

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

    subpage_types = ['NuevoIndicador']

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

class NuevoIndicador(Page):
    template = 'home/indicador.html'

    tema = models.CharField(max_length = 140)
    id_indicador = models.CharField(max_length = 140)
    medida = models.CharField(max_length = 140)
    responsable = models.CharField(max_length = 140)
    comentario = models.CharField(max_length = 500)
    estado = models.CharField(max_length = 140, help_text='Coloque alguna de las siguientes opciones: Iniciado, No Iniciado, A Validar, Concluido.')
    categoria = models.CharField(max_length = 140, help_text='Coloque alguna de las siguientes opciones: ambiental, social, economico.')
    
    parametros = StreamField([
        ('molde', blocks.StructBlock([
            ('tema', blocks.CharBlock()),
            ('id_indicador', blocks.CharBlock()),
            ('medida', blocks.CharBlock()),
            ('responsable', blocks.CharBlock()),
            ('comentario', blocks.CharBlock()),
            ('estado', blocks.ChoiceBlock(choices=[
                ('iniciado', 'Iniciado'),
                ('no_iniciado', 'No Iniciado'),
                ('a_validar', 'A Validar'),
                ('concluido', 'Concluido'),
            ])),
            ('categoria', blocks.ChoiceBlock(choices=[
                ('ambiental', 'Ambiental'),
                ('social', 'Social'),
                ('economico', 'Economico'),
            ])),
        ])),
    ], use_json_field=True)

    historial = StreamField([
        ('id_year', blocks.StructBlock([
            ('id', blocks.CharBlock()),
            ('year', blocks.CharBlock()),
        ])),
        ('parameters', blocks.StructBlock([
            ('id', blocks.CharBlock(help_text='Este input debe tener el mismo valor que el ID del año asociado.')),
            ('material', blocks.CharBlock()),
            ('valor', blocks.CharBlock()),
            ('porcentaje', blocks.CharBlock()),
        ])),
    ], use_json_field=True)

    protocolo = StreamField([
        ('molde', blocks.StructBlock([
            ('desc', blocks.CharBlock()),
            ('mater', blocks.CharBlock()),
            ('topic', blocks.CharBlock()),
            ('relev', blocks.CharBlock()),
            ('sources', blocks.CharBlock()),
        ])),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('tema', classname = 'full'),
        FieldPanel('id_indicador', classname = 'full'),
        FieldPanel('medida', classname = 'full'),
        FieldPanel('responsable', classname = 'full'),
        FieldPanel('comentario', classname = 'full'),
        FieldPanel('estado', classname = 'full'),
        FieldPanel('categoria', classname = 'full'),
        FieldPanel('historial', classname = 'full'),
        FieldPanel('protocolo', classname = 'full'),
    ]

    parent_page_types = ['Indicadores']

'''
class NuevoInforme(Page):
    template = 'home/indicador.html'

    tema_material = models.CharField(max_length = 140, default = '')
    id_indicador = models.CharField(max_length = 140, blank = False)
    medida = models.CharField(max_length = 140, blank = False)
    responsable = models.CharField(max_length = 140, blank = False)
    comentario = models.CharField(max_length = 500, blank = False)
    estado = models.CharField(max_length = 140, blank = False, help_text='Coloque alguna de las siguientes opciones: Iniciado, No Iniciado, A Validar, Concluido.')
    categoria = models.CharField(max_length = 140, blank = False, help_text='Coloque alguna de las siguientes opciones: Ambiental, Social, Economico.')

    historial = StreamField([
        ('id_year', blocks.StructBlock([
            ('id', blocks.CharBlock()),
            ('year', blocks.CharBlock()),
        ])),
        ('parameters', blocks.StructBlock([
            ('id', blocks.CharBlock(help_text='Este input debe tener el mismo valor que el ID del año asociado.')),
            ('material', blocks.CharBlock()),
            ('valor', blocks.CharBlock()),
            ('porcentaje', blocks.CharBlock()),
        ])),
    ], use_json_field=True)

    protocolo = StreamField([
        ('molde', blocks.StructBlock([
            ('desc', blocks.CharBlock()),
            ('mater', blocks.CharBlock()),
            ('topic', blocks.CharBlock()),
            ('relev', blocks.CharBlock()),
            ('sources', blocks.CharBlock()),
        ])),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('tema_material', classname = 'full'),
        FieldPanel('id_indicador', classname = 'full'),
        FieldPanel('medida', classname = 'full'),
        FieldPanel('responsable', classname = 'full'),
        FieldPanel('comentario', classname = 'full'),
        FieldPanel('estado', classname = 'full'),
        FieldPanel('categoria', classname = 'full'),
        FieldPanel('historial', classname = 'full'),
        FieldPanel('protocolo', classname = 'full'),
    ]

    parent_page_types = ['Indicadores']
'''