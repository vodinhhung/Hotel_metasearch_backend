# Generated by Django 3.1.1 on 2020-10-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20201015_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roothotel',
            name='hotel_address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='hotel_lat',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='hotel_logo',
            field=models.CharField(max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='hotel_long',
            field=models.FloatField(max_length=20, null=True),
        ),
    ]