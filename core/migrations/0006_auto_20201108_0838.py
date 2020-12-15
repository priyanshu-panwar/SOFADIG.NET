# Generated by Django 2.2.8 on 2020-11-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_utility_fax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utility',
            name='Fax',
        ),
        migrations.AddField(
            model_name='shop',
            name='latitude',
            field=models.CharField(default='00', max_length=7),
        ),
        migrations.AddField(
            model_name='shop',
            name='longitude',
            field=models.CharField(default='00', max_length=7),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='default_brand.jpg', upload_to='brands/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PCB',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
