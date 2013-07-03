# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from core.models import *
from suit_redactor.widgets import RedactorWidget
from suit.admin import SortableModelAdmin


class ArticleForm(ModelForm):
    class Meta:
        widgets = {
            'text' : RedactorWidget(editor_options={'lang': 'ru'})
        }
class ArticleAdmin(ModelAdmin):
    form = ArticleForm
    fieldsets = [
        (u'Текст статьи', {'classes': ('full-width',), 'fields': ('text',)})
    ]

class QuestionAnswerAdmin(SortableModelAdmin):
    sortable = 'order'

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(ClientType)
admin.site.register(Article, ArticleAdmin)
admin.site.register(QuoteRequest)
admin.site.register(PhoneContact)
admin.site.register(InsuranceProgramm)
admin.site.register(News)
admin.site.register(QuestionAnswer, QuestionAnswerAdmin)