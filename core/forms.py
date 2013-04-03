# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, CharField, TextInput, URLField, DateField
from django.forms.extras.widgets import SelectDateWidget
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

class FaqForm(ModelForm):
    question = CharField(widget=Textarea(attrs={'class': 'redactor'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'Вопрос', max_length=1000)
    answer = CharField(widget=Textarea(attrs={'class': 'redactor'}),
        error_messages={'required': u'Обязательное поле'},
        label=u'Ответ', max_length=2000)
    class Meta:
        model = QuestionAnswer

class NewsForm(ModelForm):
    title = CharField(widget=TextInput(attrs={'class': 'input-xxlarge', 'placeholder': u'Введите текст'}),
                      error_messages={'required': u'Обязательное поле'},
                      label=u'Заголовок новости')
    anounce = CharField(widget=Textarea(attrs={'class': 'redactor'}),
                       error_messages={'required': u'Обязательное поле'},
                       label=u'Анонс', max_length=400)
    text = CharField(widget=Textarea(attrs={'class': 'redactor'}),
                     error_messages={'required': u'Обязательное поле'},
                     label=u'Текст', max_length=2000)
    date = DateField(widget=SelectDateWidget(), label=u'Дата',
                     error_messages={'required': u'Обязательное поле'},)
    class Meta:
        model = News