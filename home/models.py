
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

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

class FlexPage(Page):
    template = 'home/indicador.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body', classname = 'full')
    ]

class SecondPage(Page):
    template = 'home/informes.html'
    subtitle = RichTextField(max_length = 100, null = True, blank = True)
    body = RichTextField(blank = True)
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body', classname = 'full')
    ]

class Meta:
    verbose_name = 'Indicador'
    verbose_name_plural = 'Indicadores'
