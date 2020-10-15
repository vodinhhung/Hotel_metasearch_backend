# Generated by Django 3.1.1 on 2020-10-15 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20201015_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roothotel',
            name='district_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.domain'),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='province_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.province'),
        ),
        migrations.AlterField(
            model_name='roothotel',
            name='street_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.street'),
        ),
    ]