# Generated by Django 4.0.6 on 2022-08-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0021_bill_print_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='print_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
