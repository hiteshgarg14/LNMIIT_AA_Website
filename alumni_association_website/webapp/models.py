from django.db import models


class Event(models.Model):
        STATUS_CHOICES = (
                ('draft', 'Draft'),
                ('live', 'Live'),
                ('finished', 'Finished'),
        )
        title = models.CharField(max_length=2000, blank=False)
        slug = models.SlugField(max_length=250, unique=True)
        presenter = models.CharField(max_length=2000, blank=True)
        presenter_position = models.CharField(max_length=2000, blank=True)
        venue = models.CharField(max_length=2000, default='')
        description = models.TextField()
        datetime = models.DateTimeField(blank=False)
        status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                                  default='draft')
