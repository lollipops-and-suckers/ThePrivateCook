# Generated by Django 3.2.8 on 2023-10-19 16:29

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_remove_testimonial_a star value is valid between 1 and 5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='stars',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[main.validators.validate_num_of_stars]),
        ),
    ]