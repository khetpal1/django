# Generated by Django 3.0.6 on 2020-09-02 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=120)),
                ('Status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'SHipped'), ('refunded', 'Refunded')], default='created', max_length=120)),
                ('shipping_Total', models.DecimalField(decimal_places=2, default=5.05, max_digits=100)),
                ('Total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.Create')),
            ],
        ),
    ]
