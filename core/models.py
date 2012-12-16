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
    name = models.CharField(max_length=100, verbose_name=u'Тип клиента')
    programms = models.ManyToManyField(InsuranceProgramm, verbose_name=u'Доступные программы')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Тип клиента'

class QuestionAnswer(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

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

class Menu(models.Model):
    alias = models.CharField(max_length=100)

class MenuItem(models.Model):
    title = models.CharField(max_length=40)
    url = models.URLField()
    availableInMenu = models.ManyToManyField(Menu)

class QuestionAnswer(models.Model):
    question = models.TextField(max_length=400, verbose_name=u'Вопрос')
    answer = models.TextField(max_length=400, verbose_name=u'Ответ')
