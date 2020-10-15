# Generated by Django 3.1.1 on 2020-10-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20201015_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roothotel',
            name='check_in',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='check_out',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='hotel_star',
            field=models.IntegerField(null=True),
        ),
    ]