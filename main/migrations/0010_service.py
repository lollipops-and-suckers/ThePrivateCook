# Generated by Django 3.2.8 on 2023-10-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('service', models.IntegerField(blank=True, default=80, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='service')),
                ('is_key_service', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
