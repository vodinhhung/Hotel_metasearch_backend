# Generated by Django 3.1.1 on 2020-10-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20201015_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roothotel',
            name='hotel_name',
            field=models.CharField(max_length=500),
        ),
    ]