# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'igame_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('publishYear', self.gf('django.db.models.fields.IntegerField')()),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('gameCode', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'igame', ['Game'])

        # Adding model 'Shop'
        db.create_table(u'igame_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('nif', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('city', self.gf('django.db.models.fields.TextField')(default=' ')),
            ('country', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shops', null=True, to=orm['igame.Game'])),
        ))
        db.send_create_signal(u'igame', ['Shop'])

        # Adding model 'Producer'
        db.create_table(u'igame_producer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nif', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('city', self.gf('django.db.models.fields.TextField')(default=' ')),
            ('country', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(related_name='producer', null=True, to=orm['igame.Game'])),
        ))
        db.send_create_signal(u'igame', ['Producer'])

        # Adding model 'gameReview'
        db.create_table(u'igame_gamereview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=5)),
            ('coment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['igame.Game'])),
        ))
        db.send_create_signal(u'igame', ['gameReview'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'igame_game')

        # Deleting model 'Shop'
        db.delete_table(u'igame_shop')

        # Deleting model 'Producer'
        db.delete_table(u'igame_producer')

        # Deleting model 'gameReview'
        db.delete_table(u'igame_gamereview')


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
        u'igame.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'gameCode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'publishYear': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'igame.gamereview': {
            'Meta': {'object_name': 'gameReview'},
            'coment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['igame.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'igame.producer': {
            'Meta': {'object_name': 'Producer'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'country': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'producer'", 'null': 'True', 'to': u"orm['igame.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'nif': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'igame.shop': {
            'Meta': {'object_name': 'Shop'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'country': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shops'", 'null': 'True', 'to': u"orm['igame.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nif': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['igame']