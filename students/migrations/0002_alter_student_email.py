# Generated by Django 4.1.5 on 2023-01-17 18:32

from django.db import migrations, models
# import core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
