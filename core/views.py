from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext
from forms import *

def main_page(request):
    return render_to_response('core/main.html')

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
    return render_to_response('core/admin/admin_article_list.html')

@permission_required('core.add_article')
def admin_article_add(request):
    return render_to_response('core/admin/admin_article_add.html')

@permission_required('core.add_article')
def admin_article_edit(request, article_id):
    return render_to_response('core/admin/admin_article_edit.html')

@permission_required('core.add_clienttype')
def admin_client_type_list(request):
    client_types = ClientType.objects.all()
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