from django import template
from core.models import *
from core.forms import *
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
    menu_items = MenuItem.objects.filter(availableInMenu=menu.id).order_by('order')
    t = loader.get_template(menu.template)
    c = Context({'items': menu_items })
    return t.render(c)

@register.inclusion_tag('core/side_type_menu.html', takes_context=True)
def show_side_menu(context, type):
    categories = Category.objects.filter(client_type__type_id=type)
    request = context['request']
    active = False

    slugs = request.path.split('/')
    private_cat = Category.objects.filter(client_type__type_id='PR')
    in_private = False
    for cat in private_cat:
        if in_private or 'personal' in slugs:
            in_private = True
            break
        in_private = cat.article.slug in slugs

    company_cat = Category.objects.filter(client_type__type_id='CP')
    in_company = False
    for cat in company_cat:
        if in_company or 'company' in slugs:
            in_company = True
            break
        in_company = cat.article.slug in slugs

    if (in_private and type == 'PR') or (in_company and type == 'CP'):
        active = True
    return {'type': type, 'items': categories, 'active': active}

@register.inclusion_tag('core/side_info_block.html', takes_context=True)
def show_info_block(context):
    articles = Article.objects.filter(is_helpful=True, is_active=True).order_by('order_helpful')[:6]
    return {'articles': articles}

@register.inclusion_tag('core/callback_form.html', takes_context=True)
def show_callback_form(context):
    form = PhoneContactForm()
    return {'callback': form }
# @register.inclusion_tag('main_menu.html', takes_context=True)
# def show_menu(context):
#     pages = Page.objects.filter(is_active = True).order_by('order')
#     return {'pages': pages}
#
# @register.inclusion_tag('bottom_menu.html', takes_context=True)
# def show_bottom_menu(context):
#     pages = Page.objects.filter(is_active = True).order_by('order')
#     return {'pages': pages}