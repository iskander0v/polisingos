# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InsuranceProgramm'
        db.create_table('core_insuranceprogramm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['InsuranceProgramm'])

        # Adding model 'MenuItem'
        db.create_table('core_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('core', ['MenuItem'])

        # Adding M2M table for field availableInMenu on 'MenuItem'
        db.create_table('core_menuitem_availableInMenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menuitem', models.ForeignKey(orm['core.menuitem'], null=False)),
            ('menu', models.ForeignKey(orm['core.menu'], null=False))
        ))
        db.create_unique('core_menuitem_availableInMenu', ['menuitem_id', 'menu_id'])

        # Adding model 'QuoteRequest'
        db.create_table('core_quoterequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('leadName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('programm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.InsuranceProgramm'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('core', ['QuoteRequest'])

        # Adding model 'QuestionAnswer'
        db.create_table('core_questionanswer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['QuestionAnswer'])

        # Adding model 'ClientType'
        db.create_table('core_clienttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['ClientType'])

        # Adding M2M table for field programms on 'ClientType'
        db.create_table('core_clienttype_programms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clienttype', models.ForeignKey(orm['core.clienttype'], null=False)),
            ('insuranceprogramm', models.ForeignKey(orm['core.insuranceprogramm'], null=False))
        ))
        db.create_unique('core_clienttype_programms', ['clienttype_id', 'insuranceprogramm_id'])

        # Adding model 'PhoneContact'
        db.create_table('core_phonecontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('callInTime', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('core', ['PhoneContact'])

        # Adding model 'Menu'
        db.create_table('core_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Menu'])

        # Adding model 'Article'
        db.create_table('core_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('core', ['Article'])


    def backwards(self, orm):
        # Deleting model 'InsuranceProgramm'
        db.delete_table('core_insuranceprogramm')

        # Deleting model 'MenuItem'
        db.delete_table('core_menuitem')

        # Removing M2M table for field availableInMenu on 'MenuItem'
        db.delete_table('core_menuitem_availableInMenu')

        # Deleting model 'QuoteRequest'
        db.delete_table('core_quoterequest')

        # Deleting model 'QuestionAnswer'
        db.delete_table('core_questionanswer')

        # Deleting model 'ClientType'
        db.delete_table('core_clienttype')

        # Removing M2M table for field programms on 'ClientType'
        db.delete_table('core_clienttype_programms')

        # Deleting model 'PhoneContact'
        db.delete_table('core_phonecontact')

        # Deleting model 'Menu'
        db.delete_table('core_menu')

        # Deleting model 'Article'
        db.delete_table('core_article')


    models = {
        'core.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'slug': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.menu': {
            'Meta': {'object_name': 'Menu'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'availableInMenu': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Menu']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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