# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Metric.source_ip'
        db.add_column(u'metrics_metric', 'source_ip',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Metric.source_ip'
        db.delete_column(u'metrics_metric', 'source_ip')


    models = {
        u'metrics.metric': {
            'Meta': {'unique_together': "(('source', 'name'),)", 'object_name': 'Metric'},
            '_previous_counter_value': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'alert_operator': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'alert_triggered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alert_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'display_as': ('django.db.models.fields.CharField', [], {'default': "'float'", 'max_length': '20'}),
            'friendly_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_counter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'latest_value': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['metrics.Source']", 'null': 'True'}),
            'source_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'transform': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'metrics.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['metrics']