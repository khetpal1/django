# Generated by Django 3.0.6 on 2020-09-17 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20200910_1352'),
        ('orders', '0002_auto_20200910_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billlingprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='billing.BIllingProfile'),
        ),
    ]
