# Generated by Django 5.1 on 2024-08-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_redactor_years_of_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redactor',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
