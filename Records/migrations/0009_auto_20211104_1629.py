# Generated by Django 3.2.9 on 2021-11-04 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0008_rename_post_postimage_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='DateOfDelivery',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='record',
            name='DateOfOrderTaken',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
