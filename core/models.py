from django.db import models

class InsuranceProgramm(models.Model):
    name = models.CharField(max_length=100)
    slug = models.URLField()
    description = models.TextField()

class ClientType(models.Model):
    name = models.CharField(max_length=100)
    programms = models.ManyToManyField(InsuranceProgramm)

class QuestionAnswer(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

class PhoneContact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    callInTime = models.TimeField()

class QuoteRequest(models.Model):
    leadName = models.CharField(max_length=100)
    programm = models.ManyToOneRel(InsuranceProgramm)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.URLField()

class Menu(models.Model):
    alias = models.CharField(max_length=100)

class MenuItem(models.Model):
    title = models.CharField(max_length=40)
    url = models.URLField()
    availableInMenu = models.ManyToManyField(Menu)