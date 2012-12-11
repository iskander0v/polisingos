# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, CharField, TextInput, URLField
from models import *

class InsuranceProgrammForm(ModelForm):
    description = CharField(widget=Textarea(attrs={'class': 'redactor'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'Описание')
    name = CharField(widget=TextInput(attrs={'class': 'input-xxlarge', 'placeholder': u'Введите текст'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'Название программы')
    slug = CharField(widget=TextInput(attrs={'class': 'input-xxlarge', 'placeholder': u'Введите адрес'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'URL адрес')
    class Meta:
        model = InsuranceProgramm

class ClientTypeForm(ModelForm):
    class Meta:
        model = ClientType

class ArticleForm(ModelForm):
    title = CharField(widget=TextInput(attrs={'class': 'input-xxlarge', 'placeholder': u'Введите текст'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'Заголовок статьи')
    slug = CharField(widget=TextInput(attrs={'class': 'input-xxlarge', 'placeholder': u'Введите адрес'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'URL адрес')
    text = CharField(widget=Textarea(attrs={'class': 'redactor'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'Текст статьи')
    class Meta:
        model = Article