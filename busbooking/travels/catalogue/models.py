from django.db import models

# Create your models here.
class City(models.Model):    
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name

class Stop(models.Model):    
    name = models.CharField(max_length=31)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='stops')

    def __str__(self):
        return self.name


class Route(models.Model):    
    name = models.CharField(max_length=31)
    origin = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='origins')
    destination = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='destinations')
    distance = models.DecimalField(max_digits=6, decimal_places=1)

class Facility(models.Model):
    facility =  models.CharField(max_length=31)


class MiddleStop(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='links')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='middle_stops')
    origin_distance =   models.DecimalField(max_digits=6, decimal_places=1)
    destination_distance =   models.DecimalField(max_digits=6, decimal_places=1)
    facility =  models.ManyToManyField(Facility)


class BusType(models.Model):
    bus_type =  models.CharField(max_length=31)

class Bus(models.Model):
    name = models.CharField(max_length=31)
    bus_type = models.ForeignKey(BusType, on_delete=models.CASCADE, related_name='busses')
    facility =  models.ManyToManyField(Facility)

class SeatType(models.Model):
    seat_type = models.CharField(max_length=31)

class Seating(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='seats')
    seat_no = models.PositiveSmallIntegerField ()
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE, related_name='seating')
    occupancy = models.PositiveSmallIntegerField()

DAYS = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))


class Service(models.Model):
    
	bus_type = models.ForeignKey(BusType, on_delete=models.CASCADE, related_name='services')
	route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route_services')
	start_time = models.TimeField()
	end_time = models.TimeField()

class ServiceStop(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_stops')
	middle_stop = models.ForeignKey(MiddleStop, on_delete=models.CASCADE, related_name='middle_stop_services')
	scheduled_arrival = models.TimeField()
	scheduled_departure = models.TimeField()
	


class ServiceDay(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_days')
    day = models.CharField(max_length=12, choices=DAYS)
