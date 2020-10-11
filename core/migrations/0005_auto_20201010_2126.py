# Generated by Django 2.2.8 on 2020-10-10 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201010_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientlist',
            name='INGREDIENTS',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='AMT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ING_LIST',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.IngredientList'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='NAME',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
