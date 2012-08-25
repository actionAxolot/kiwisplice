# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FinancialChannel'
        db.create_table('prospection_financialchannel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('financial_institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.FinancialInstitution'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('prospection', ['FinancialChannel'])

        # Adding model 'ProspectionMedia'
        db.create_table('prospection_prospectionmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('prospection', ['ProspectionMedia'])

        # Adding model 'ProspectionChannel'
        db.create_table('prospection_prospectionchannel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('media', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prospection.ProspectionMedia'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('prospection', ['ProspectionChannel'])

        # Adding model 'Prospection'
        db.create_table('prospection_prospection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='salesperson', to=orm['account.Profile'])),
            ('prospect', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prospect', to=orm['account.Profile'])),
            ('financial_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prospection.FinancialChannel'])),
            ('prospection_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prospection.ProspectionChannel'])),
            ('visitation_date', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('prospection', ['Prospection'])


    def backwards(self, orm):
        # Deleting model 'FinancialChannel'
        db.delete_table('prospection_financialchannel')

        # Deleting model 'ProspectionMedia'
        db.delete_table('prospection_prospectionmedia')

        # Deleting model 'ProspectionChannel'
        db.delete_table('prospection_prospectionchannel')

        # Deleting model 'Prospection'
        db.delete_table('prospection_prospection')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventory.financialinstitution': {
            'Meta': {'object_name': 'FinancialInstitution'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'prospection.financialchannel': {
            'Meta': {'object_name': 'FinancialChannel'},
            'financial_institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.FinancialInstitution']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'prospection.prospection': {
            'Meta': {'object_name': 'Prospection'},
            'financial_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prospection.FinancialChannel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prospect': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prospect'", 'to': "orm['account.Profile']"}),
            'prospection_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prospection.ProspectionChannel']"}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'salesperson'", 'to': "orm['account.Profile']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'visitation_date': ('django.db.models.fields.DateField', [], {})
        },
        'prospection.prospectionchannel': {
            'Meta': {'object_name': 'ProspectionChannel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prospection.ProspectionMedia']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'prospection.prospectionmedia': {
            'Meta': {'object_name': 'ProspectionMedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['prospection']