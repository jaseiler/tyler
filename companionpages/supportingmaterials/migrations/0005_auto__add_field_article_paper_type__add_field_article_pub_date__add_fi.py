# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.paper_type'
        db.add_column(u'supportingmaterials_article', 'paper_type',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=45),
                      keep_default=False)

        # Adding field 'Article.pub_date'
        db.add_column(u'supportingmaterials_article', 'pub_date',
                      self.gf('django.db.models.fields.DateField')(default='2009-12-10'),
                      keep_default=False)

        # Adding field 'Article.volume'
        db.add_column(u'supportingmaterials_article', 'volume',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Article.issue'
        db.add_column(u'supportingmaterials_article', 'issue',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Article.pages'
        db.add_column(u'supportingmaterials_article', 'pages',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Article.keywords'
        db.add_column(u'supportingmaterials_article', 'keywords',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Article.research_area'
        db.add_column(u'supportingmaterials_article', 'research_area',
                      self.gf('django.db.models.fields.CharField')(default='32', max_length=100),
                      keep_default=False)

        # Adding field 'Article.research_area_2'
        db.add_column(u'supportingmaterials_article', 'research_area_2',
                      self.gf('django.db.models.fields.CharField')(default='32', max_length=100),
                      keep_default=False)

        # Adding field 'Article.authors'
        db.add_column(u'supportingmaterials_article', 'authors',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)

        # Adding field 'Article.coders'
        db.add_column(u'supportingmaterials_article', 'coders',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)


        # Changing field 'Article.doi'
        db.alter_column(u'supportingmaterials_article', 'doi', self.gf('django.db.models.fields.CharField')(default='',max_length=500))

        # Changing field 'Article.title'
        db.alter_column(u'supportingmaterials_article', 'title', self.gf('django.db.models.fields.CharField')(default='',max_length=500))

        # Changing field 'Article.abstract_text'
        db.alter_column(u'supportingmaterials_article', 'abstract_text', self.gf('django.db.models.fields.TextField')(default='',max_length=2000))

    def backwards(self, orm):
        # Deleting field 'Article.paper_type'
        db.delete_column(u'supportingmaterials_article', 'paper_type')

        # Deleting field 'Article.pub_date'
        db.delete_column(u'supportingmaterials_article', 'pub_date')

        # Deleting field 'Article.volume'
        db.delete_column(u'supportingmaterials_article', 'volume')

        # Deleting field 'Article.issue'
        db.delete_column(u'supportingmaterials_article', 'issue')

        # Deleting field 'Article.pages'
        db.delete_column(u'supportingmaterials_article', 'pages')

        # Deleting field 'Article.keywords'
        db.delete_column(u'supportingmaterials_article', 'keywords')

        # Deleting field 'Article.research_area'
        db.delete_column(u'supportingmaterials_article', 'research_area')

        # Deleting field 'Article.research_area_2'
        db.delete_column(u'supportingmaterials_article', 'research_area_2')

        # Deleting field 'Article.authors'
        db.delete_column(u'supportingmaterials_article', 'authors')

        # Deleting field 'Article.coders'
        db.delete_column(u'supportingmaterials_article', 'coders')


        # Changing field 'Article.doi'
        db.alter_column(u'supportingmaterials_article', 'doi', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'Article.title'
        db.alter_column(u'supportingmaterials_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Article.abstract_text'
        db.alter_column(u'supportingmaterials_article', 'abstract_text', self.gf('django.db.models.fields.TextField')(max_length=500))

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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
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
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'biography': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'gravatar_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'supportingmaterials.article': {
            'Meta': {'object_name': 'Article'},
            'abstract_text': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'article_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'coders': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'corresponding_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'paper_type': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '45'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'research_area': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'research_area_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'supportingmaterials.supportingmaterial': {
            'Meta': {'object_name': 'SupportingMaterial'},
            'archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'companion_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['supportingmaterials.Article']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'explanatory_text': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"})
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
        }
    }

    complete_apps = ['supportingmaterials']