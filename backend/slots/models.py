# Create your models here.
from django.db import models

from base.models import SimpleModel
from resources.models import Resource


class ReservedSlot(SimpleModel):
    resource = models.ForeignKey(
        Resource,
        verbose_name="resource",
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        verbose_name="name",
        max_length=30,
        null=False,
    )

    description = models.CharField(
        verbose_name="description",
        max_length=1000,
        null=False,
    )

    email = models.EmailField(
        verbose_name="email",
        null=False,
    )

    start_time = models.DateTimeField(
        verbose_name="start_time",
        null=False,
    )

    end_time = models.DateTimeField(
        verbose_name="end_time",
        null=False,
    )

    class Meta:
        verbose_name = "reserved_slot"
        verbose_name_plural = "reserved_slots"
        ordering = ("start_time",)
