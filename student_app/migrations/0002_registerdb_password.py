# Generated by Django 4.1.1 on 2023-03-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdb',
            name='password',
            field=models.CharField(default='', max_length=10),
        ),
    ]
