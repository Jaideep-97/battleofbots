# Generated by Django 3.0.1 on 2020-01-02 13:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_profile_weapons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='weapons',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
