# Generated by Django 2.2.8 on 2020-12-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_utility_success_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='Conditions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='utility',
            name='Politique',
            field=models.TextField(default=''),
        ),
    ]