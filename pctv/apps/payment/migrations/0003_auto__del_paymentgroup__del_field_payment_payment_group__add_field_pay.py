# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PaymentGroup'
        db.delete_table('payment_paymentgroup')

        # Deleting field 'Payment.payment_group'
        db.delete_column('payment_payment', 'payment_group_id')

        # Adding field 'Payment.client'
        db.add_column('payment_payment', 'client',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['client.Client']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PaymentGroup'
        db.create_table('payment_paymentgroup', (
            ('date_closed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client.Client'])),
            ('date_created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('payment', ['PaymentGroup'])

        # Adding field 'Payment.payment_group'
        db.add_column('payment_payment', 'payment_group',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['payment.PaymentGroup']),
                      keep_default=False)

        # Deleting field 'Payment.client'
        db.delete_column('payment_payment', 'client_id')


    models = {
        'account.profile': {
            'Meta': {'object_name': 'Profile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'default': '1', 'to': "orm['auth.User']", 'unique': 'True', 'blank': 'True'})
        },
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
        'client.client': {
            'Meta': {'object_name': 'Client'},
            'auth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'delivery_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Inventory']", 'null': 'True', 'blank': 'True'}),
            'notary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'pricing_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'prospection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prospection.Prospection']"}),
            'signature_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Sin cliente'", 'max_length': '50'})
        },
        'comment.comment': {
            'Meta': {'object_name': 'Comment'},
            'commenter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Profile']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventory.inventory': {
            'Meta': {'object_name': 'Inventory'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'clg_emission_date': ('django.db.models.fields.DateField', [], {}),
            'construction_end_date': ('django.db.models.fields.DateField', [], {}),
            'construction_size': ('django.db.models.fields.IntegerField', [], {}),
            'construction_status': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'cuv': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
        },
        'payment.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client.Client']"}),
            'date_due': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_payed': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'prospection.prospection': {
            'Meta': {'object_name': 'Prospection'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'father_lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'financial_channel': ('django.db.models.fields.CharField', [], {'default': "'IMSS'", 'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'mother_lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'municipality': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'prospection_channel': ('django.db.models.fields.CharField', [], {'default': "'Fraccionamiento'", 'max_length': '50'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'salesperson'", 'to': "orm['auth.User']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'total_income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'visitation_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['payment']