from django.shortcuts import render

from menu_app.models import Menu


def menu(request, slug):
    menu_item = Menu.objects.get(url=slug)
    context = {
        'menu_name': menu_item.title,
        'slug': menu_item.url
    }
    return render(request, 'menu.html', context)
