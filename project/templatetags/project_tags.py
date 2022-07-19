from django import template

from project.models import Language

register = template.Library()


@register.simple_tag()
def get_languages():
    return Language.objects.all()
