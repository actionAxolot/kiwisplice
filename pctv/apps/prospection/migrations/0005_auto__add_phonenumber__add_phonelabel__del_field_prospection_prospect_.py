# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhoneNumber'
        db.create_table('prospection_phonenumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prospection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prospection.Prospection'])),
            ('phone_label', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prospection.PhoneLabel'])),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('prospection', ['PhoneNumber'])

        # Adding model 'PhoneLabel'
        db.create_table('prospection_phonelabel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('prospection', ['PhoneLabel'])

        # Deleting field 'Prospection.prospect'
        db.delete_column('prospection_prospection', 'prospect_id')

        # Adding field 'Prospection.first_name'
        db.add_column('prospection_prospection', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Prospection.middle_name'
        db.add_column('prospection_prospection', 'middle_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Prospection.father_lastname'
        db.add_column('prospection_prospection', 'father_lastname',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Prospection.mother_lastname'
        db.add_column('prospection_prospection', 'mother_lastname',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Prospection.email'
        db.add_column('prospection_prospection', 'email',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Prospection.street'
        db.add_column('prospection_prospection', 'street',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Prospection.block'
        db.add_column('prospection_prospection', 'block',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Prospection.postal_code'
        db.add_column('prospection_prospection', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Prospection.municipality'
        db.add_column('prospection_prospection', 'municipality',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Prospection.state'
        db.add_column('prospection_prospection', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Prospection.total_income'
        db.add_column('prospection_prospection', 'total_income',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2),
                      keep_default=False)


        # Changing field 'Prospection.salesperson'
        db.alter_column('prospection_prospection', 'salesperson_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Profile']))

    def backwards(self, orm):
        # Deleting model 'PhoneNumber'
        db.delete_table('prospection_phonenumber')

        # Deleting model 'PhoneLabel'
        db.delete_table('prospection_phonelabel')

        # Adding field 'Prospection.prospect'
        db.add_column('prospection_prospection', 'prospect',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='prospect', to=orm['account.Profile']),
                      keep_default=False)

        # Deleting field 'Prospection.first_name'
        db.delete_column('prospection_prospection', 'first_name')

        # Deleting field 'Prospection.middle_name'
        db.delete_column('prospection_prospection', 'middle_name')

        # Deleting field 'Prospection.father_lastname'
        db.delete_column('prospection_prospection', 'father_lastname')

        # Deleting field 'Prospection.mother_lastname'
        db.delete_column('prospection_prospection', 'mother_lastname')

        # Deleting field 'Prospection.email'
        db.delete_column('prospection_prospection', 'email')

        # Deleting field 'Prospection.street'
        db.delete_column('prospection_prospection', 'street')

        # Deleting field 'Prospection.block'
        db.delete_column('prospection_prospection', 'block')

        # Deleting field 'Prospection.postal_code'
        db.delete_column('prospection_prospection', 'postal_code')

        # Deleting field 'Prospection.municipality'
        db.delete_column('prospection_prospection', 'municipality')

        # Deleting field 'Prospection.state'
        db.delete_column('prospection_prospection', 'state')

        # Deleting field 'Prospection.total_income'
        db.delete_column('prospection_prospection', 'total_income')


        # Changing field 'Prospection.salesperson'
        db.alter_column('prospection_prospection', 'salesperson_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

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
        'prospection.phonelabel': {
            'Meta': {'object_name': 'PhoneLabel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'prospection.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_label': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prospection.PhoneLabel']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'prospection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prospection.Prospection']"})
        },
        'prospection.prospection': {
            'Meta': {'object_name': 'Prospection'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'father_lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'financial_channel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'mother_lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'municipality': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'salesperson'", 'to': "orm['account.Profile']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'total_income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
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