# Generated by Django 2.2.8 on 2020-11-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_utility_fax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utility',
            name='Fax',
        ),
        migrations.AddField(
            model_name='utility',
            name='PresentationHeading',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='PresentationPara1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='PresentationPara2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='PresentationPara3',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='TopHeading',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='TopParagraph',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='utility',
            name='TopSubHeading',
            field=models.CharField(default='', max_length=500),
        ),
    ]
