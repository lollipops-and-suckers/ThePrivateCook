# Generated by Django 3.2.8 on 2023-10-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20231008_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='contact_number',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
