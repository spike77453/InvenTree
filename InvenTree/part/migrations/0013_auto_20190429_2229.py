# Generated by Django 2.2 on 2019-04-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0012_part_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='URL',
            field=models.URLField(blank=True, help_text='Link to external URL'),
        ),
    ]
