# Generated by Django 3.0.3 on 2020-03-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('File_Name', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('Observer_Name', models.CharField(max_length=20)),
            ],
        ),
    ]
