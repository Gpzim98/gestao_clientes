from django import template

register = template.Library()

@register.filter
def arredonda(value, casas):
    return round(value, casas)
