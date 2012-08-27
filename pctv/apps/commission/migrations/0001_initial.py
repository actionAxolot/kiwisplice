# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CommissionGroup'
        db.create_table('commission_commissiongroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payment_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['payment.PaymentGroup'])),
            ('cancellation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('commission', ['CommissionGroup'])

        # Adding model 'Commission'
        db.create_table('commission_commission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commission.CommissionGroup'])),
            ('payment_date', self.gf('django.db.models.fields.DateField')()),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('commission', ['Commission'])


    def backwards(self, orm):
        # Deleting model 'CommissionGroup'
        db.delete_table('commission_commissiongroup')

        # Deleting model 'Commission'
        db.delete_table('commission_commission')


    models = {
        'account.profile': {
            'Meta': {'object_name': 'Profile'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'total_income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
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
            'auth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'delivery_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integration_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'notary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'pricing_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Profile']"}),
            'signature_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'comment.comment': {
            'Meta': {'object_name': 'Comment'},
            'commenter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Profile']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'commission.commission': {
            'Meta': {'object_name': 'Commission'},
            'commission_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commission.CommissionGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'commission.commissiongroup': {
            'Meta': {'object_name': 'CommissionGroup'},
            'cancellation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['payment.PaymentGroup']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'payment.paymentgroup': {
            'Meta': {'object_name': 'PaymentGroup'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client.Client']"}),
            'date_closed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['commission']