# Generated by Django 3.2.9 on 2021-11-03 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0003_record_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='Photo',
        ),
    ]
