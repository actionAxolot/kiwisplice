# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FinancialChannelClient.value'
        db.delete_column('finance_financialchannelclient', 'value')

        # Adding field 'FinancialChannelClient.amount'
        db.add_column('finance_financialchannelclient', 'amount',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)

        # Deleting field 'FinancialChannelInventory.value'
        db.delete_column('finance_financialchannelinventory', 'value')

        # Adding field 'FinancialChannelInventory.amount'
        db.add_column('finance_financialchannelinventory', 'amount',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'FinancialChannelClient.value'
        db.add_column('finance_financialchannelclient', 'value',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Deleting field 'FinancialChannelClient.amount'
        db.delete_column('finance_financialchannelclient', 'amount')

        # Adding field 'FinancialChannelInventory.value'
        db.add_column('finance_financialchannelinventory', 'value',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Deleting field 'FinancialChannelInventory.amount'
        db.delete_column('finance_financialchannelinventory', 'amount')


    models = {
        'finance.financialchannelclient': {
            'Meta': {'object_name': 'FinancialChannelClient'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'financial_institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.FinancialInstitution']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '50'})
        },
        'finance.financialchannelinventory': {
            'Meta': {'object_name': 'FinancialChannelInventory'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'financial_institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.FinancialInstitution']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '50'})
        },
        'finance.financialinstitution': {
            'Meta': {'object_name': 'FinancialInstitution'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['finance']