from django import template

register = template.Library()


@register.filter()
def my_media(val):
    if val:
        return f'shop/images/{val}'

    return '#'
