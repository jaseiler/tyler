# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'compendia_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('status', self.gf('model_utils.fields.StatusField')(default='draft', max_length=100, no_check_for_status=True)),
            ('status_changed', self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor=u'status')),
            ('site_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('authorship', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('abstract', self.gf('django.db.models.fields.TextField')(max_length=5000, blank=True)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('article_url', self.gf('django.db.models.fields.URLField')(max_length=2000, blank=True)),
            ('article_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('legacy_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('doi', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('primary_research_field', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('secondary_research_field', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('notes_for_staff', self.gf('django.db.models.fields.TextField')(max_length=5000, blank=True)),
        ))
        db.send_create_signal(u'compendia', ['Article'])

        # Adding model 'Contributor'
        db.create_table(u'compendia_contributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compendia.Article'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('citation_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'compendia', ['Contributor'])

        # Adding model 'SupportingMaterial'
        db.create_table(u'compendia_supportingmaterial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('status', self.gf('model_utils.fields.StatusField')(default='draft', max_length=100, no_check_for_status=True)),
            ('status_changed', self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor=u'status')),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compendia.Article'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('archive_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=5000, blank=True)),
            ('materials_url', self.gf('django.db.models.fields.URLField')(max_length=2000, blank=True)),
            ('description_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('materials_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'compendia', ['SupportingMaterial'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'compendia_article')

        # Deleting model 'Contributor'
        db.delete_table(u'compendia_contributor')

        # Deleting model 'SupportingMaterial'
        db.delete_table(u'compendia_supportingmaterial')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'compendia.article': {
            'Meta': {'ordering': "['title']", 'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            'article_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'article_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'}),
            'authorship': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contributors'", 'symmetrical': 'False', 'through': u"orm['compendia.Contributor']", 'to': u"orm['users.User']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'notes_for_staff': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            'primary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'secondary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'compendia.contributor': {
            'Meta': {'ordering': "['citation_order', 'user']", 'object_name': 'Contributor'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compendia.Article']"}),
            'citation_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'compendia.supportingmaterial': {
            'Meta': {'ordering': "['name']", 'object_name': 'SupportingMaterial'},
            'archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compendia.Article']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            'description_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'materials_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'affiliation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['compendia']