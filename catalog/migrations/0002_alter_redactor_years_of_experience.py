# Generated by Django 5.1 on 2024-08-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redactor',
            name='years_of_experience',
            field=models.IntegerField(default=0),
        ),
    ]
