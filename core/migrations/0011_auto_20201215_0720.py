# Generated by Django 2.2.8 on 2020-12-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_utility_fax'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='contact_mail',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='contact_subject',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='utility',
            name='info_mail',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='info_subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]