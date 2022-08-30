from django import template

register = template.Library()

@register.filter
def job_to_dictionary(h, key):
    return h[key]