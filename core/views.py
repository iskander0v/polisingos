from django.shortcuts import render_to_response
from django.contrib.auth.decorators import permission_required

def main_page(request):
    return render_to_response('core/main.html')

@permission_required('core.add_insuranceprogramm')
def admin_insurance_programm_list(request):
    return render_to_response('core/admin/admin_insurance_programm_list.html')

@permission_required('core.add_insuranceprogramm')
def admin_insurance_programm_add(request):
    return render_to_response('core/admin/admin_insurance_programm_add.html')

@permission_required('core.add_insuranceprogramm')
def admin_insurance_programm_edit(request, insurance_programm_id):
    return render_to_response('core/admin/admin_insurance_programm_edit.html')

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
    return render_to_response('core/admin/admin_client_type_list.html')