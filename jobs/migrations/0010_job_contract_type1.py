# Generated by Django 4.0.7 on 2022-10-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_job_contract_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='contract_type1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]