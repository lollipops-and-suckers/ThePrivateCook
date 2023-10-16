# Generated by Django 3.2.8 on 2023-10-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230924_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='bio',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='title',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='heroImage',
            field=models.ImageField(blank=True, null=True, upload_to='heroImage'),
        ),
    ]