from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,str):
    return  value.replace(str,'')
#register.filter('cut',cut)