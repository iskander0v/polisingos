from django import template
from core.models import *
from django.template import loader, Context

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'class="active"'
    return ''

@register.simple_tag
def show_menu(textid):
    menu = Menu.objects.get(textid=textid)
    menu_items = MenuItem.objects.filter(availableInMenu=menu.id)
    t = loader.get_template(menu.template)
    c = Context({'items': menu_items })
    return t.render(c)

@register.inclusion_tag('core/side_type_menu.html', takes_context=True)
def show_side_menu(context, type):
    categories = Category.objects.filter(client_type__type_id=type)
    request = context['request']
    active = False
    if (request.path.find('personal') != -1 and type == 'PR') or (request.path.find('company') != -1 and type == 'CP'):
        active = True
    return {'type': type, 'items': categories, 'active': active}


# @register.inclusion_tag('main_menu.html', takes_context=True)
# def show_menu(context):
#     pages = Page.objects.filter(is_active = True).order_by('order')
#     return {'pages': pages}
#
# @register.inclusion_tag('bottom_menu.html', takes_context=True)
# def show_bottom_menu(context):
#     pages = Page.objects.filter(is_active = True).order_by('order')
#     return {'pages': pages}