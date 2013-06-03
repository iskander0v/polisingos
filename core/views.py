# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext, Context
from django.template.loader import get_template
from forms import *
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail
from django.utils import simplejson



def main_page(request):
    news = News.objects.all().order_by('-date')[:5]
    article_about = Article.objects.get(slug = 'about-word-bupa')
    return render_to_response('core/main.html',
                              {'news': news, 'article_about': article_about},
                              context_instance = RequestContext(request))

def personal_page(request):
    categories = Category.objects.filter(client_type__type_id='PR').order_by('order')
    return render_to_response('core/personal_page.html',
                              {'categories': categories},
                              context_instance = RequestContext(request))

def company_page(request):
    categories = Category.objects.filter(client_type__type_id='CP').order_by('order')
    article = Article.objects.get(slug = 'profit_for_company')
    return render_to_response('core/company_page.html',
                              {'categories': categories, 'article': article},
                              context_instance = RequestContext(request))

def news(request):
    news = News.objects.all().order_by('-date')
    return render_to_response('core/news.html',
                              {'news': news},
                              context_instance = RequestContext(request))

def news_item(request, id):
    news_item = get_object_or_404(News, pk=id)
    return render_to_response('core/news_item.html',
                              {'item': news_item},
                              context_instance = RequestContext(request))

def filtered_news(request, year=2013, month=None):
    news = []
    for item in News.objects.all():
        if month != None:
            if item.date.month >= int(month) and item.date.year >= int(year):
                news.append(item)
        else:
            news.append(item)

    return render_to_response('core/news.html',
                              {'news': news},
                              context_instance = RequestContext(request))

def articles(request):
    articles = Article.objects.filter(in_helpful_category=True, is_active=True)
    return render_to_response('core/article_list.html',
                              { 'articles': articles },
                              context_instance = RequestContext(request))

def article(request, slug):
    article = Article.objects.get(slug=slug, is_active=True)
    return render_to_response('core/article.html',
                              {'article':article},
                              context_instance = RequestContext(request))

def category(request, slug):
    cat = Category.objects.filter(article__slug=slug, article__is_active=True)[0]
    return render_to_response('core/category.html',
                              {'category': cat},
                              context_instance = RequestContext(request))

def calculate(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            subject = u'Bupolis.ru - Заказ на расчет полиса'

            send_mail(
                subject,
                get_template('core/quote_email.html').render(
                    Context({
                        'quote': quote,
                    })
                ),
                'info@bupolis.ru',
                ['info@polis-ingos.ru', 'roman.iskanderov@gmail.com'],
                fail_silently = False
            )

            return HttpResponseRedirect(reverse('core.views.main_page'))
    else:
        form = QuoteForm()
    return render_to_response('core/request_form.html',
        {'form': form},
        context_instance = RequestContext(request))

def faq(request):
    faqs = QuestionAnswer.objects.all();
    return render_to_response('core/faq.html',
        {'faqs': faqs},
        context_instance = RequestContext(request))

def contacts(request):
    article = get_object_or_404(Article, slug='uridich_info')
    return render_to_response('core/contacts.html', {'article':article}, context_instance=RequestContext(request))

def programms(request):
    article = Article.objects.get(slug = 'programm-introduction')
    return render_to_response('core/programms.html', {'article':article}, context_instance=RequestContext(request))

def programm(request, id):
    programm = get_object_or_404(InsuranceProgramm, pk=id)
    return render_to_response('core/programm.html', {'programm':programm}, context_instance=RequestContext(request))

def callback(request):
    context = {}
    if request.is_ajax():
        if request.method == 'POST':
            name = request.POST['name'].strip()
            phone = request.POST['phone'].strip()
            subject = u'Bupolis.ru - Запрос на обратный звонок'

            send_mail(
                subject,
                get_template('core/callback_email.html').render(
                    Context({
                        'name': name,
                        'phone': phone
                        })
                ),
                'info@bupolis.ru',
                ['info@polis-ingos.ru', 'roman.iskanderov@gmail.com'],
                fail_silently = False
            )
    return HttpResponse(context)

def admin_main(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            from django.contrib.auth import login
            login(request, form.get_user())
            if '/account/logout/' in request.get_full_path():
                return HttpResponseRedirect('/')

    else:
        form = AuthenticationForm(request)

    return render_to_response('core/admin/admin_login.html', {'form': form}, context_instance=RequestContext(request))

@permission_required('core.add_insuranceprogramm')
def admin_insurance_programm_list(request):
    iprogramms = InsuranceProgramm.objects.all().order_by('id')
    return render_to_response('core/admin/admin_insurance_programm_list.html',
        {'programms': iprogramms},
        context_instance= RequestContext(request))

@permission_required('core.add_insuranceprogramm')
def admin_insurance_programm_add(request):
    if request.method == 'POST':
        form = InsuranceProgrammForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_insurance_programm_list'))
    else:
        form = InsuranceProgrammForm()
    return render_to_response('core/admin/admin_insurance_programm_add.html',
        {'form':form},
        context_instance=RequestContext(request))

@permission_required('core.add_insuranceprogramm')
def admin_insurance_programm_edit(request, programm_id):
    iprogramm = get_object_or_404(InsuranceProgramm, pk = programm_id)
    if request.method == 'POST':
        form = InsuranceProgrammForm(request.POST, instance=iprogramm)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_insurance_programm_list'))
    else:
        form = InsuranceProgrammForm(instance=iprogramm)
    return render_to_response('core/admin/admin_insurance_programm_edit.html',
        {'form': form, 'programm': iprogramm},
        context_instance=RequestContext(request))

@permission_required('core.add_article')
def admin_article_list(request):
    articles = Article.objects.all().order_by('id')
    return render_to_response('core/admin/admin_article_list.html',
        {'articles': articles},
        context_instance=RequestContext(request))

@permission_required('core.add_article')
def admin_article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_article_list'))
    else:
        form = ArticleForm()
    return render_to_response('core/admin/admin_article_add.html',
        {'form':form},
        context_instance=RequestContext(request))

@permission_required('core.add_article')
def admin_article_edit(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_article_list'))
    else:
        form = ArticleForm(instance=article)
    return render_to_response('core/admin/admin_article_edit.html',
        {'form': form, 'article': article},
        context_instance=RequestContext(request))

@permission_required('core.add_clienttype')
def admin_client_type_list(request):
    client_types = ClientType.objects.all().order_by('id')
    return render_to_response('core/admin/admin_client_type_list.html',
        {'client_types': client_types},
        context_instance=RequestContext(request))

@permission_required('core.add_clienttype')
def admin_client_type_add(request):
    if request.method == 'POST':
        form = ClientTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_client_type_list'))
    else:
        form = ClientTypeForm()
    return render_to_response('core/admin/admin_client_type_add.html',
        {'form': form},
        context_instance=RequestContext(request))

@permission_required('core.add_clienttype')
def admin_client_type_edit(request, client_type_id):
    client_type = get_object_or_404(ClientType, pk=client_type_id)
    if request.method == 'POST':
        form = ClientTypeForm(request.POST, instance=client_type)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_client_type_list'))
    else:
        form = ClientTypeForm(instance=client_type)
    return render_to_response('core/admin/admin_client_type_edit.html',
        {'form': form, 'client_type': client_type},
        context_instance = RequestContext(request))

@permission_required('core.add_questionanswer')
def admin_faq_list(request):
    faqs = QuestionAnswer.objects.all().order_by('id')
    return render_to_response('core/admin/admin_faq_list.html',
        {'faqs': faqs},
        context_instance=RequestContext(request))

@permission_required('core.add_questionanswer')
def admin_faq_add(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_faq_list'))
    else:
        form = FaqForm()
    return render_to_response('core/admin/admin_faq_add.html',
        {'form': form},
        context_instance=RequestContext(request))

@permission_required('core.add_questionanswer')
def admin_faq_edit(request, faq_id):
    faq = get_object_or_404(QuestionAnswer, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_faq_list'))
    else:
        form = FaqForm(instance=faq)
    return render_to_response('core/admin/admin_faq_edit.html',
        {'form': form, 'faq': faq},
        context_instance = RequestContext(request))

@permission_required('core.add_news')
def admin_news_list(request):
    news = News.objects.all().order_by('id')
    return render_to_response('core/admin/admin_news_list.html',
                          {'news': news},
                          context_instance=RequestContext(request))

@permission_required('core.add_news')
def admin_news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_news_list'))
    else:
        form = NewsForm()
    return render_to_response('core/admin/admin_news_add.html',
                              {'form': form},
                              context_instance=RequestContext(request))

@permission_required('core.add_news')
def admin_news_edit(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core.views.admin_news_list'))
    else:
        form = NewsForm(instance=news)
    return render_to_response('core/admin/admin_news_edit.html',
                              {'form': form, 'news': news},
                              context_instance = RequestContext(request))