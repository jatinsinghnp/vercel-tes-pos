# Generated by Django 4.0.6 on 2022-07-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_delete_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='company_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
