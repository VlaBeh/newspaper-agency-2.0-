# Generated by Django 4.2.9 on 2024-09-04 07:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_redactor_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='publishers',
            field=models.ManyToManyField(related_name='redactors', to=settings.AUTH_USER_MODEL),
        ),
    ]
