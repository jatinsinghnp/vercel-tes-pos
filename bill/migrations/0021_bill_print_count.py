# Generated by Django 4.0.6 on 2022-08-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0020_tablreturnentry_unit_tblsalesentry_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='print_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
