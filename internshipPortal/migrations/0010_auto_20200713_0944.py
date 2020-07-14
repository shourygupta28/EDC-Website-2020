# Generated by Django 3.0.8 on 2020-07-13 09:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('internshipPortal', '0009_auto_20200712_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venturecapitalist',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Add country code before the contact no.', max_length=128, null=True, region=None),
        ),
    ]