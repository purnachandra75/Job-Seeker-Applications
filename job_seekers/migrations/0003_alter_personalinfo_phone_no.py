# Generated by Django 5.1 on 2024-10-19 08:18

import job_seekers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0002_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='Phone_no',
            field=models.BigIntegerField(validators=[job_seekers.models.validate_phone_number]),
        ),
    ]