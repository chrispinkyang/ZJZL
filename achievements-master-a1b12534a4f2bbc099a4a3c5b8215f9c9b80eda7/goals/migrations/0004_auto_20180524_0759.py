# Generated by Django 2.0.4 on 2018-05-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_transactionrecord_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goalStatus',
            field=models.SmallIntegerField(choices=[(-1, '失败'), (0, '待激活'), (1, '进行中'), (2, '完成')], default=0, help_text='-1:失败,0:待激活,1:进行中,2:完成', verbose_name='目标状态'),
        ),
    ]
