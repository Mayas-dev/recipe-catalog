from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
# Create your models here.



class RecipePage(Page):
    description = models.TextField()
    ingredients = RichTextField(
        blank=True
    )
    method = RichTextField(
        blank=True
    )
    origin = models.CharField(
        max_length=100,
        blank=True
    )
    calories = models.IntegerField(
        null=True,
        blank=True
    )
    prep_time = models.IntegerField(
        null=True,
        blank=True,
        help_text="Minutes"
    )

    cook_time = models.IntegerField(
        null=True,
        blank=True,
        help_text="Minutes"
    )

    servings = models.IntegerField(
        null=True,
        blank=True
    )
    disclaimer = models.TextField(
    blank=True
    )

    featured_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("ingredients"),
        FieldPanel("method"),
        FieldPanel("origin"),
        FieldPanel("calories"),
        FieldPanel("prep_time"),
        FieldPanel("cook_time"),
        FieldPanel("servings"),
        FieldPanel("disclaimer"),
        FieldPanel("featured_image"),
    ]










#class RecipePage(Page):
#    description = models.TextField()
#    ingredients = RichTextField()
#    method = RichTextField()
#    origin = models.CharField(max_length=500)
#    nutrition = RichTextField()
#    disclaimer = models.TextField()
#    content_panels = Page.content_panels + [
#        FieldPanel("description"),
#        FieldPanel("ingredients"),
#        FieldPanel("method"),
#        FieldPanel("origin"),
#        FieldPanel("nutrition"),
#        FieldPanel("disclaimer"),
#    ]