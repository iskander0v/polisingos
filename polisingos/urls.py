from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.main_page', name='home'),
    (r'^back/', include('core.admin_url')),
    url(r'personal/', 'core.views.personal_page', name='personal'),
    url(r'company/', 'core.views.company_page', name='company'),
    url(r'news/$', 'core.views.news', name='news'),
    url(r'news-item/(?P<id>\w+)/$', 'core.views.news_item', name='news_item'),
    url(r'news/(?P<year>\d{4})/$', 'core.views.filtered_news', name='filtered_news'),
    url(r'news/(?P<year>\d{4})/(?P<month>\d{2})/$', 'core.views.filtered_news', name='filtered_news'),
    url(r'^articles/$', 'core.views.articles', name='articles'),
    url(r'^article/(?P<slug>[A-Za-z0-9_-]+)/$', 'core.views.article', name='article'),
    url(r'^category/(?P<slug>[A-Za-z0-9_-]+)/$', 'core.views.category', name='category'),
    url(r'^order/calculate/$', 'core.views.calculate', name='calculate'),
    url(r'^faq/$', 'core.views.faq', name='faq'),
    url(r'^contacts/$', 'core.views.contacts', name='contacts'),
    url(r'^contacts/callback$', 'core.views.callback', name='callback'),
    url(r'^programms/$', 'core.views.programms', name='programms'),
    url(r'^programms/(?P<id>\w+)/$', 'core.views.programm', name='programm'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
