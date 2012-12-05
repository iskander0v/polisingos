from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.main_page', name='home'),
    url(r'^back/$', 'core.views.admin_insurance_programm_list', name='admin_home'),
    url(r'^back/content/programm/$', 'core.views.admin_insurance_programm_list', name='admin_insurance_programm'),
    url(r'^back/content/client-type/$', 'core.views.admin_client_type_list', name='admin_client_type'),
    url(r'^back/content/article/$', 'core.views.admin_article_list', name='admin_article'),
    url(r'^back/content/$', 'core.views.admin_insurance_programm_list', name='admin_insurance_programm'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
