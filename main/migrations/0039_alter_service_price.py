# Generated by Django 3.2.8 on 2023-10-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_aboutus_mywhatsappurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
