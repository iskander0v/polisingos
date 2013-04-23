# -*- coding: utf-8 -*-
from django.forms import *
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


class QuoteForm(ModelForm):
    client_type = ChoiceField(widget=RadioSelect, initial='F', choices=QuoteRequest.QUOTE_TYPE, label=u'')
    name = CharField(widget=TextInput(attrs={'class': 'input-text input-text-313-32'}),
                                error_messages={'required': u'Обязательное поле'},label=u'Имя')
    contact_name = CharField(widget=TextInput(attrs={'class': 'input-text input-text-313-32'}),
                                error_messages={'required': u'Обязательное поле'},label=u'Контактная информация')
    email_or_phone = CharField(widget=TextInput(attrs={'class': 'input-text input-text-313-32'}),
                                error_messages={'required': u'Обязательное поле'},label=u'Телефон или E-mail')
    country = CharField(widget=TextInput(attrs={'class': 'input-text input-text-313-32'}),
                                error_messages={'required': u'Обязательное поле'},label=u'Основная страна пребывания')
    client_age = IntegerField(widget=TextInput(attrs={'class': 'input-text input-text-313-32'}),
                                error_messages={'required': u'Обязательное поле'},label=u'Возраст')
    comment = CharField(required=False,  widget=Textarea(attrs={'class': 'textarea-text', 'rows': '6', 'cols': '90'}), label=u'Ваши комментарии и пожелания')

    def clean(self):
        cleaned_data = super(QuoteForm, self).clean()
        client_type = cleaned_data.get("client_type", None)

        if client_type is None:
            return cleaned_data

        contact_name = cleaned_data.get("contact_name", None)
        client_age = cleaned_data.get("client_age", None)

        if client_type == 'C' and client_age is None:
            del self._errors["client_age"]
        if client_type == 'F' and contact_name is None:
            del self._errors["contact_name"]

        # Always return the full collection of cleaned data.
        return cleaned_data

    class Meta:
        model = QuoteRequest