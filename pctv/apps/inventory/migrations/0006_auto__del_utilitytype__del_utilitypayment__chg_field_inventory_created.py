# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UtilityType'
        db.delete_table('inventory_utilitytype')

        # Deleting model 'UtilityPayment'
        db.delete_table('inventory_utilitypayment')


        # Changing field 'Inventory.created_by'
        db.alter_column('inventory_inventory', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

    def backwards(self, orm):
        # Adding model 'UtilityType'
        db.create_table('inventory_utilitytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('inventory', ['UtilityType'])

        # Adding model 'UtilityPayment'
        db.create_table('inventory_utilitypayment', (
            ('payment_date', self.gf('django.db.models.fields.DateField')()),
            ('utility_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.UtilityType'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Inventory'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('inventory', ['UtilityPayment'])


        # Changing field 'Inventory.created_by'
        db.alter_column('inventory_inventory', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2012, 9, 18, 0, 0), to=orm['auth.User']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventory.bridgecredit': {
            'Meta': {'object_name': 'BridgeCredit'},
            'approved_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'approved_on': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Inventory']"}),
            'ministered_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '30'})
        },
        'inventory.bridgecreditpayment': {
            'Meta': {'object_name': 'BridgeCreditPayment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'bridge_credit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.BridgeCredit']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {})
        },
        'inventory.inventory': {
            'Meta': {'object_name': 'Inventory'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'clg_emission_date': ('django.db.models.fields.DateField', [], {}),
            'construction_end_date': ('django.db.models.fields.DateField', [], {}),
            'construction_size': ('django.db.models.fields.IntegerField', [], {}),
            'construction_status': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'cuv': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lot_size': ('django.db.models.fields.IntegerField', [], {}),
            'macro_lot': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'official_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'percent_completed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'prototype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Prototype']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Section']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'inventory.prototype': {
            'Meta': {'object_name': 'Prototype'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'inventory.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['inventory']