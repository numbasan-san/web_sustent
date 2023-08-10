
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from rest_framework.fields import Field
from wagtail.images.api.fields import ImageRenditionField

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

class ImageSerializationField(Field):
    
    def to_representation(self, value):
        return {
            "url": value.file.url,
            "title": value.title,
            "width": value.width,
            "height": value.height,
        }
