
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

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
    subpages_types = ["IndicadorDetalles"]
    #  "IndicadorFormulario", "IndicadorGrafico", "IndicadorParametros"

class Indicador(Page):
    template = 'home/indicador.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    corp = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('corp', classname = 'full'),
        FieldPanel('body', classname = 'full')
    ]

class IndicadorFormulario(Page):
    template = 'home/form_validacion.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    corp = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('corp', classname = 'full'),
        FieldPanel('body', classname = 'full')
    ]

class IndicadorGrafico(Page):
    template = 'home/indicador_grafico.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    corp = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('corp', classname = 'full'),
        FieldPanel('body', classname = 'full')
    ]

class IndicadorParametros(Page):
    template = 'home/indicador_parametros.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    corp = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('corp', classname = 'full'),
        FieldPanel('body', classname = 'full')
    ]

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

class ParametroIndicador(Page):
    template = 'home/test.html'
    codigo = RichTextField(blank = False)
    atributo = RichTextField(blank = False)
    content_panels = Page.content_panels + [
        FieldPanel('codigo'),
        FieldPanel('atributo'),
    ]

class Meta:
    verbose_name = 'Indicador'
    verbose_name_plural = 'Indicadores'
