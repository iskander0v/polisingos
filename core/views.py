from django.shortcuts import render_to_response
from django.contrib.auth.decorators import permission_required

def main_page(request):
    return render_to_response('core/main.html')

@permission_required('core.add_insuranceprogramm')
def admin_insurance_programm(request):
    return render_to_response('core/admin/admin_insurance_programm_list.html')