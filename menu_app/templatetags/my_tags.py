from django import template
from django.urls import reverse

from menu_app.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_title):
    menu_items = Menu.objects.filter(title=menu_title)
    print()
    print(Menu.objects.get(id=1).title)
    print(Menu.objects.get(id=1).children.values())
    # print(menu_items.values())

    menu_endpoint = 'temp2'

    def dfs(all_urls, menu_items):
        for item in menu_items:
            if item == menu_endpoint:
                return all_urls
            all_urls.append(item)
            dfs(all_urls, item.children.all())

    menu_items_list = dfs([], menu_items)
    # print(menu_items_list)
    print()
    return draw_menu_items(menu_items, 0)


def draw_menu_items(menu_items, count):
    if not menu_items:
        return ''
    result = '<ul>'
    # def dfs(menu_items, url, level):
    #
    # dfs(menu_items, 'temp2')
    # print(menu_items)
    for item in menu_items:
        print('---' * count, item.title)
        result += f'<li><a href="{reverse("menu", kwargs={"slug": item.url})}">{item.title}</a>'
        result += draw_menu_items(item.children.all(), count + 1)
        result += '</li>'
    result += '</ul>'
    return result

# print('<li><a href="{% url "menu" ' + f'{item.url}' + ' %}">' + f'{item.title}</a>')
# @register.simple_tag(takes_context=True)
# def draw_menu(context, menu_name):
#     request = context['request']
#     current_url = request.path
#
#     menu_items = Menu.objects.filter(title=menu_name).prefetch_related('children')
#
#     def render_menu_item(item):
#         active = current_url == item.url or current_url.startswith(reverse('menu', kwargs={"slug": item.url}))
#         children = item.children.all()
#         if children:
#             children_html = ''.join([render_menu_item(child) for child in children])
#             return f'<li class="{"active" if active else ""}"><a href="{reverse("menu", kwargs={"slug": item.url})}">\
#             {item.title}</a><ul>{children_html}</ul></li>'
#         else:
#             return f'<li class="{"active" if active else ""}"><a href="{reverse("menu", kwargs={"slug": item.url})}">\
#             {item.title}</a></li>'
#
#     menu_html = ''.join([render_menu_item(item) for item in menu_items])
#     return f'<ul>{menu_html}</ul>'
