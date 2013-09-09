# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'QuestionAnswer.order'
        db.add_column('core_questionanswer', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'QuestionAnswer.order'
        db.delete_column('core_questionanswer', 'order')


    models = {
        'core.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_helpful_category': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_helpful': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_helpful': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'short_descr': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'core.clienttype': {
            'Meta': {'object_name': 'ClientType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'programms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.InsuranceProgramm']", 'symmetrical': 'False'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'core.insuranceprogramm': {
            'Meta': {'object_name': 'InsuranceProgramm'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'table': ('django.db.models.fields.TextField', [], {})
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
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Article']", 'null': 'True', 'blank': 'True'}),
            'availableInMenu': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Menu']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.questionanswer': {
            'Meta': {'object_name': 'QuestionAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '1000'})
        },
        'core.quoterequest': {
            'Meta': {'object_name': 'QuoteRequest'},
            'client_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'client_type': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "u'\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f'", 'max_length': '50'}),
            'email_or_phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']