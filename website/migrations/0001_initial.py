# Generated by Django 2.0.3 on 2018-10-10 21:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('tag', models.CharField(choices=[('P_S1', 'Parrot Senario 1'), ('P_S2', 'Parrot Senario 2'), ('P_M', 'Parrot Movment'), ('W', 'Weel')], max_length=4)),
                ('arg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('login_status', models.BooleanField(default=False)),
                ('last_activity', models.BigIntegerField(default=0)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('first_name', 'last_name', 'phone_number')},
        ),
    ]
