# Generated by Django 5.1 on 2024-11-06 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0011_rename_applicants_applicant'),
        ('usercredintials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='usercredintials.userdetails'),
            preserve_default=False,
        ),
    ]