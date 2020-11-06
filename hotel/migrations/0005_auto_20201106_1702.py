# Generated by Django 3.1.2 on 2020-11-06 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20201106_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='quality',
            name='num_review',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quality',
            name='review_score',
            field=models.FloatField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='root',
            name='min_price_domain',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='min_price',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='info',
            name='root',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hotel.root'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='overall_score',
            field=models.FloatField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='quality',
            name='root',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hotel.root'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('domain_hotel_id', models.CharField(max_length=100)),
                ('langcode', models.CharField(max_length=10)),
                ('date_time', models.CharField(max_length=50)),
                ('title', models.TextField(null=True)),
                ('text', models.TextField(null=True)),
                ('score', models.FloatField(max_length=5)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.domain')),
                ('root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.root')),
            ],
        ),
    ]