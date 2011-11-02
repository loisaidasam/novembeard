# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('web_profile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('vanity', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('web', ['Profile'])

        # Adding model 'ProfileComment'
        db.create_table('web_profilecomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profile_user', to=orm['auth.User'])),
            ('commenter', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='commenter', null=True, to=orm['auth.User'])),
            ('commenter_ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('web', ['ProfileComment'])

        # Adding model 'Photo'
        db.create_table('web_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('internal_path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('web_path', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('web', ['Photo'])

        # Adding model 'PhotoComment'
        db.create_table('web_photocomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Photo'])),
            ('commenter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('commenter_ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('web', ['PhotoComment'])

        # Adding model 'PhotoRating'
        db.create_table('web_photorating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Photo'])),
            ('rater', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('rater_ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('web', ['PhotoRating'])


    def backwards(self, orm):
        
        # Deleting model 'Profile'
        db.delete_table('web_profile')

        # Deleting model 'ProfileComment'
        db.delete_table('web_profilecomment')

        # Deleting model 'Photo'
        db.delete_table('web_photo')

        # Deleting model 'PhotoComment'
        db.delete_table('web_photocomment')

        # Deleting model 'PhotoRating'
        db.delete_table('web_photorating')


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
        'web.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'web_path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'web.photocomment': {
            'Meta': {'object_name': 'PhotoComment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'commenter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'commenter_ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Photo']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'web.photorating': {
            'Meta': {'object_name': 'PhotoRating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Photo']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'rater': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'rater_ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        'web.profile': {
            'Meta': {'object_name': 'Profile'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'vanity': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        'web.profilecomment': {
            'Meta': {'object_name': 'ProfileComment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'commenter': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'commenter'", 'null': 'True', 'to': "orm['auth.User']"}),
            'commenter_ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile_user'", 'to': "orm['auth.User']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']
