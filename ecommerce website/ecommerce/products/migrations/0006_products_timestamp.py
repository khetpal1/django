# Generated by Django 3.0.6 on 2020-08-17 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200810_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]