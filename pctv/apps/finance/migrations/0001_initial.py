# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FinancialInstitution'
        db.create_table('finance_financialinstitution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('finance', ['FinancialInstitution'])

        # Adding model 'FinancialChannelInventory'
        db.create_table('finance_financialchannelinventory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('financial_institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.FinancialInstitution'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='pending', max_length=50)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('finance', ['FinancialChannelInventory'])

        # Adding model 'FinancialChannelClient'
        db.create_table('finance_financialchannelclient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('financial_institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.FinancialInstitution'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='pending', max_length=50)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('finance', ['FinancialChannelClient'])


    def backwards(self, orm):
        # Deleting model 'FinancialInstitution'
        db.delete_table('finance_financialinstitution')

        # Deleting model 'FinancialChannelInventory'
        db.delete_table('finance_financialchannelinventory')

        # Deleting model 'FinancialChannelClient'
        db.delete_table('finance_financialchannelclient')


    models = {
        'finance.financialchannelclient': {
            'Meta': {'object_name': 'FinancialChannelClient'},
            'financial_institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.FinancialInstitution']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '50'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'finance.financialchannelinventory': {
            'Meta': {'object_name': 'FinancialChannelInventory'},
            'financial_institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.FinancialInstitution']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '50'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'finance.financialinstitution': {
            'Meta': {'object_name': 'FinancialInstitution'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['finance']