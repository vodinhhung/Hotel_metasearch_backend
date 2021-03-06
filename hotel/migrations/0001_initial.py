# Generated by Django 3.1.2 on 2020-11-06 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('index', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('index', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('index', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('index', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500, null=True)),
                ('logo', models.CharField(max_length=2083, null=True)),
                ('lat', models.FloatField(max_length=20, null=True)),
                ('long', models.FloatField(max_length=20, null=True)),
                ('star', models.IntegerField(null=True)),
                ('check_in', models.CharField(max_length=20, null=True)),
                ('check_out', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(null=True)),
                ('street', models.CharField(max_length=500, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.district')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.province')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('index', models.IntegerField()),
                ('root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hotel.root')),
                ('have_breakfast', models.IntegerField()),
                ('is_free_wifi', models.IntegerField()),
                ('have_car_park', models.IntegerField()),
                ('have_airport_transport', models.IntegerField()),
                ('have_restaurant', models.IntegerField()),
                ('have_deposit', models.IntegerField()),
                ('have_baby_service', models.IntegerField()),
                ('have_bar', models.IntegerField()),
                ('have_laundry', models.IntegerField()),
                ('have_tour', models.IntegerField()),
                ('have_spa', models.IntegerField()),
                ('have_pool', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('index', models.IntegerField()),
                ('root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hotel.root')),
                ('cleanliness_scores', models.FloatField(max_length=5)),
                ('meal_score', models.FloatField(max_length=5)),
                ('location_score', models.FloatField(max_length=5)),
                ('sleep_quality_score', models.FloatField(max_length=5)),
                ('room_score', models.FloatField(max_length=5)),
                ('service_score', models.FloatField(max_length=5)),
                ('facility_score', models.FloatField(max_length=5)),
                ('overall_score', models.FloatField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('domain_hotel_id', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=2083)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.domain')),
                ('root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.root')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('index', models.IntegerField()),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.district')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.province')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.province'),
        ),
    ]
