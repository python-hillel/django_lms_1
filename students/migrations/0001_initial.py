# Generated by Django 4.1.5 on 2023-01-17 17:49

import datetime
import django.core.validators
from django.db import migrations, models
import core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='f_name', max_length=50, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='First name')),
                ('last_name', models.CharField(db_column='l_name', max_length=50, verbose_name='Last name')),
                ('age', models.PositiveIntegerField()),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(max_length=254, validators=[core.validators.validate_email_domain])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
