# Generated by Django 2.2.8 on 2020-12-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201130_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='Fax',
            field=models.CharField(default='+590 (0) 590 26 73 21', max_length=100),
        ),
    ]
