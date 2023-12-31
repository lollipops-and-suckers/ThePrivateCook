# Generated by Django 3.2.8 on 2023-10-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='chefs')),
                ('twitterURL', models.CharField(blank=True, max_length=500, null=True)),
                ('facebookURL', models.CharField(blank=True, max_length=500, null=True)),
                ('instagramURL', models.CharField(blank=True, max_length=500, null=True)),
                ('linkedinURL', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Chef',
                'verbose_name_plural': 'Chefs',
                'ordering': ['name'],
            },
        ),
    ]
