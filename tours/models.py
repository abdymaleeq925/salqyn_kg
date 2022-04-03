from django.db import models


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
        ("In pending", TOUR_STATUS_WAITING),
        ("In process", TOUR_STATUS_START),
        ("Finished", TOUR_STATUS_COMPLETED),
        ("Canceled", TOUR_STATUS_CANCELED)
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
