from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter(name='split')
def split(value, key):
    return value.split(key)