from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    try:
        value = float(value)
        arg = float(arg)
        result = value * arg
        return round(result, 2)
    except (ValueError, TypeError):
        return value

