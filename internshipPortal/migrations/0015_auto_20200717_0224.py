# Generated by Django 3.0.7 on 2020-07-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internshipPortal', '0014_auto_20200716_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venturecapitalist',
            name='about',
            field=models.CharField(max_length=550),
        ),
    ]