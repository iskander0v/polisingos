from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext
from forms import *

def main_page(request):
    return render_to_response('core/main.html')

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