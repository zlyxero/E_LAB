# Generated by Django 2.0.1 on 2018-01-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0010_auto_20180131_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='member_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='insurance member id'),
        ),
    ]