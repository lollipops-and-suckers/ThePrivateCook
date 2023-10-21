# Generated by Django 3.2.8 on 2023-10-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20231015_1800'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['timestamp'], 'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image_booking',
            field=models.ImageField(blank=True, null=True, upload_to='AboutUsImages'),
        ),
    ]