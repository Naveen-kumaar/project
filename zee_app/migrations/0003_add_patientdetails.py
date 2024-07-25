# Generated by Django 5.0.7 on 2024-07-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zee_app', '0002_alter_register_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_patientdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('Occupation', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Contactno', models.IntegerField()),
                ('Chief_complaint', models.CharField(max_length=100)),
                ('Injury', models.CharField(max_length=100)),
                ('History', models.CharField(max_length=100)),
                ('Pain', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Duration', models.TimeField()),
                ('Onset', models.CharField(max_length=100)),
                ('A_factor', models.CharField(max_length=100)),
                ('R_factor', models.CharField(max_length=100)),
                ('On_palpation', models.CharField(max_length=100)),
                ('Special_test', models.CharField(max_length=100)),
                ('Treatment', models.CharField(max_length=100)),
            ],
        ),
    ]
