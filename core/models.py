# -*- coding: utf-8 -*-
from django.db import models

class InsuranceProgramm(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название программы')
    slug = models.SlugField(verbose_name=u'URL адрес')
    description = models.TextField(verbose_name=u'Описание')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Программа страхования'

class ClientType(models.Model):
    CLIENT_TYPE_IDS = (
        ('PR', 'Private'),
        ('CP', 'Companies'),
    )
    name = models.CharField(max_length=100, verbose_name=u'Тип клиента')
    programms = models.ManyToManyField(InsuranceProgramm, verbose_name=u'Доступные программы')
    type_id = models.CharField(max_length=2, choices=CLIENT_TYPE_IDS)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Тип клиента'

class PhoneContact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    callInTime = models.TimeField()

class QuoteRequest(models.Model):
    leadName = models.CharField(max_length=100)
    programm = models.ForeignKey(InsuranceProgramm)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    is_helpful = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=40)
    short_descr = models.CharField(max_length=140)
    article = models.ForeignKey(Article)
    client_type = models.ForeignKey(ClientType)
    image_name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Menu(models.Model):
    alias = models.CharField(max_length=100)
    textid = models.CharField(max_length=20, unique=True)
    template = models.CharField(max_length=40)

    def __unicode__(self):
        return self.alias

class MenuItem(models.Model):
    title = models.CharField(max_length=40)
    url = models.SlugField(null=True, blank=True)
    article = models.ForeignKey(Article, null=True, blank=True)
    availableInMenu = models.ManyToManyField(Menu)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class QuestionAnswer(models.Model):
    question = models.TextField(verbose_name=u'Вопрос', max_length=1000)
    answer = models.TextField(verbose_name=u'Ответ', max_length=2000)

    def __unicode__(self):
        return self.question

class News(models.Model):
    title = models.CharField(max_length=200)
    anounce = models.TextField(max_length=400)
    text = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return self.title