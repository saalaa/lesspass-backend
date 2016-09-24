# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-24 08:13
from __future__ import unicode_literals

from django.db import migrations

from api.data_migrations import create_password_with


def mv_entries_to_password(apps, schema_editor):
    Entry = apps.get_model("api", "Entry")
    for entry in Entry.objects.all():
        create_password_with(entry)


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_password'),
    ]

    operations = [
        migrations.RunPython(mv_entries_to_password),
    ]