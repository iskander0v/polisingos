from django.conf.urls import *

urlpatterns = patterns('core.views',
    url(r'^$', 'admin_insurance_programm_list', name='admin_home'),
    url(r'^content/$', 'admin_insurance_programm_list', name='admin_insurance_programm_list'),
    url(r'^content/article/$', 'admin_article_list', name='admin_article_list'),
    url(r'^content/article/add$', 'admin_article_add', name='admin_article_add'),
    url(r'^content/article/(?P<article_id>\d+)/$', 'admin_article_edit', name='admin_article_edit'),
    url(r'^content/client-type/$', 'admin_client_type_list', name='admin_client_type_list'),
    url(r'^content/client-type/add$', 'admin_client_type_add', name='admin_client_type_add'),
    url(r'^content/client-type/(?P<client_type_id>\d+)/$', 'admin_client_type_edit', name='admin_client_type_edit'),
    url(r'^content/programm/$', 'admin_insurance_programm_list', name='admin_insurance_programm_list'),
    url(r'^content/programm/add$', 'admin_insurance_programm_add', name='admin_insurance_programm_add'),
    url(r'^content/programm/(?P<programm_id>\d+)/$', 'admin_insurance_programm_edit', name='admin_insurance_programm_edit'),
)