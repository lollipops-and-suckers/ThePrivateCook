# Generated by Django 3.2.8 on 2023-10-08 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_aboutus_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='is_active',
        ),
    ]