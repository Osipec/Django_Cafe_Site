# Generated by Django 4.1.5 on 2023-02-15 14:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_tablereserv_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablereserv',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tablereserv',
            name='time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tablereserv',
            name='user_email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tablereserv',
            name='user_phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Wrong number', regex='^\\+?3?8?0\\d{2}[- ]?(\\d[ -]?){7}$')]),
        ),
    ]
