# Generated by Django 2.0.4 on 2018-05-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20180524_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionrecord',
            name='description',
            field=models.CharField(blank=True, max_length=4096, null=True, verbose_name='交易描述'),
        ),
    ]
