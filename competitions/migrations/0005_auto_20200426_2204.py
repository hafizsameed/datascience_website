# Generated by Django 2.0.7 on 2020-04-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_auto_20200425_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.TextField(blank=True, null=True),
        ),
    ]
