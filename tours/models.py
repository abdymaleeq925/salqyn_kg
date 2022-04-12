from django.db import models
from django.contrib.auth.models import User


class Tour(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="tours/")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("Active", default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class RegularTour(models.Model):
    TOUR_STATUS_WAITING = 'waiting'
    TOUR_STATUS_START = 'start'
    TOUR_STATUS_COMPLETED = 'completed'
    TOUR_STATUS_CANCELED = 'canceled'
    TOUR_STATUSES = (
        (TOUR_STATUS_WAITING, "In pending"),
        (TOUR_STATUS_START, "In process"),
        (TOUR_STATUS_COMPLETED, "Finished"),
        (TOUR_STATUS_CANCELED, "Canceled")
    )

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    start = models.DateTimeField("Start")
    end = models.DateTimeField("End")
    places_count = models.PositiveSmallIntegerField("Quantity of people")
    status = models.CharField("Status", choices=TOUR_STATUSES, default=TOUR_STATUS_WAITING, max_length=10)

    class Meta:
        ordering = ['-start']

    def __str__(self):
        return f"{self.tour.title} - {self.start}"


class TourBooking(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED = "confirmed"
    STATUS_FINISHED = "finished"
    STATUS_CANCELLED = "cancelled"
    BOOKING_STATUSES = (
        (STATUS_NEW, "New" ),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_FINISHED, "Finished")
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    regular_tour = models.ForeignKey(RegularTour, on_delete=models.DO_NOTHING)
    mobile = models.CharField("Mobile phone number", max_length=9)
    place_count = models.PositiveSmallIntegerField("Places")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField("Status", choices=BOOKING_STATUSES, default=STATUS_NEW, max_length=9)
    is_paid = models.BooleanField("Paid", default=False)
    notice = models.CharField("Additional information", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Your booking ID: {self.id}"
