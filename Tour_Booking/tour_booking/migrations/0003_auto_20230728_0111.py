# Generated by Django 3.2.20 on 2023-07-28 06:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tour_booking', '0002_auto_20230725_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='date',
        ),
        migrations.AddField(
            model_name='tour',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tour',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
