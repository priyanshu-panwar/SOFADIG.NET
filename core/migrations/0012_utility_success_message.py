# Generated by Django 2.2.8 on 2020-12-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201215_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='success_message',
            field=models.CharField(default='', max_length=500),
        ),
    ]
