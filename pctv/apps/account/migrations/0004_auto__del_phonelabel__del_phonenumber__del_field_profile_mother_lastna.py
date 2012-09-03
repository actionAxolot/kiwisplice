# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PhoneLabel'
        db.delete_table('account_phonelabel')

        # Deleting model 'PhoneNumber'
        db.delete_table('account_phonenumber')

        # Deleting field 'Profile.mother_lastname'
        db.delete_column('account_profile', 'mother_lastname')

        # Deleting field 'Profile.municipality'
        db.delete_column('account_profile', 'municipality')

        # Deleting field 'Profile.street'
        db.delete_column('account_profile', 'street')

        # Deleting field 'Profile.postal_code'
        db.delete_column('account_profile', 'postal_code')

        # Deleting field 'Profile.first_name'
        db.delete_column('account_profile', 'first_name')

        # Deleting field 'Profile.middle_name'
        db.delete_column('account_profile', 'middle_name')

        # Deleting field 'Profile.father_lastname'
        db.delete_column('account_profile', 'father_lastname')

        # Deleting field 'Profile.total_income'
        db.delete_column('account_profile', 'total_income')

        # Deleting field 'Profile.state'
        db.delete_column('account_profile', 'state')

        # Deleting field 'Profile.email'
        db.delete_column('account_profile', 'email')

        # Deleting field 'Profile.block'
        db.delete_column('account_profile', 'block')


    def backwards(self, orm):
        # Adding model 'PhoneLabel'
        db.create_table('account_phonelabel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('account', ['PhoneLabel'])

        # Adding model 'PhoneNumber'
        db.create_table('account_phonenumber', (
            ('phone_label', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.PhoneLabel'])),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Profile'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('account', ['PhoneNumber'])

        # Adding field 'Profile.mother_lastname'
        db.add_column('account_profile', 'mother_lastname',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Profile.municipality'
        db.add_column('account_profile', 'municipality',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Profile.street'
        db.add_column('account_profile', 'street',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Profile.postal_code'
        db.add_column('account_profile', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Profile.first_name'
        db.add_column('account_profile', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Profile.middle_name'
        db.add_column('account_profile', 'middle_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Profile.father_lastname'
        db.add_column('account_profile', 'father_lastname',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Profile.total_income'
        db.add_column('account_profile', 'total_income',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2),
                      keep_default=False)

        # Adding field 'Profile.state'
        db.add_column('account_profile', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Profile.email'
        db.add_column('account_profile', 'email',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Profile.block'
        db.add_column('account_profile', 'block',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['account']