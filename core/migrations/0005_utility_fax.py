# Generated by Django 2.2.8 on 2020-10-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='Fax',
            field=models.CharField(default='+590 (0) 590 26 73 20', max_length=100),
        ),
    ]
