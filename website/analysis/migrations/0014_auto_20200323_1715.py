# Generated by Django 3.0.3 on 2020-03-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0013_auto_20200323_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Cam_ID',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='result',
            name='Week_Num',
            field=models.CharField(default='', max_length=2),
        ),
    ]
