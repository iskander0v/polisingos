# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('core_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('short_descr', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Article'])),
            ('client_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ClientType'])),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('core', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('core_category')


    models = {
        'core.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.category': {
            'Meta': {'object_name': 'Category'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Article']"}),
            'client_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ClientType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_descr': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'core.clienttype': {
            'Meta': {'object_name': 'ClientType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'programms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.InsuranceProgramm']", 'symmetrical': 'False'})
        },
        'core.insuranceprogramm': {
            'Meta': {'object_name': 'InsuranceProgramm'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'core.menu': {
            'Meta': {'object_name': 'Menu'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'textid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'core.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'availableInMenu': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Menu']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.news': {
            'Meta': {'object_name': 'News'},
            'anounce': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.phonecontact': {
            'Meta': {'object_name': 'PhoneContact'},
            'callInTime': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.questionanswer': {
            'Meta': {'object_name': 'QuestionAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '1000'})
        },
        'core.quoterequest': {
            'Meta': {'object_name': 'QuoteRequest'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leadName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'programm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.InsuranceProgramm']"})
        }
    }

    complete_apps = ['core']