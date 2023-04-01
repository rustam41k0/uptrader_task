from django import template
from django.urls import reverse

from menu_app.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_title):
    menu_items = Menu.objects.filter(title=menu_title)
    return draw_menu_items(menu_items)


def draw_menu_items(menu_items):
    if not menu_items:
        return ''
    result = '<ul>'
    for item in menu_items:
        result += f'<li><a href="{reverse("menu", kwargs={"slug": item.url})}">{item.title}</a>'
        result += draw_menu_items(item.children.all())
        result += '</li>'
    result += '</ul>'
    return result
