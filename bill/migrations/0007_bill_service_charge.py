# Generated by Django 4.0.6 on 2022-07-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0006_bill_terminal'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='service_charge',
            field=models.FloatField(default=0.0),
        ),
    ]
