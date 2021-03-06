# Generated by Django 2.0.1 on 2018-01-29 16:17

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='insurance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.Insurance', verbose_name='insurance company'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
    ]
