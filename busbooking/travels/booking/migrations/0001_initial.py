# Generated by Django 3.1.3 on 2020-11-16 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0001_initial'),
        ('people', '0001_initial'),
        ('price_availability', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_cancelled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='booking.booking')),
            ],
        ),
        migrations.CreateModel(
            name='BookingService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('bus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='runs', to='catalogue.bus')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_services', to='catalogue.service')),
            ],
        ),
        migrations.CreateModel(
            name='BookingCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_costs', to='booking.booking')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_costs', to='price_availability.price')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.bookingservice'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='people.customer'),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_service_availability', to='booking.bookingservice')),
            ],
        ),
    ]
