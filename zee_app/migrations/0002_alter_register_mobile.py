# Generated by Django 5.0.7 on 2024-07-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zee_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
