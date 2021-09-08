from django.db import models


class Point(models.Model):
    """This class represents a Point.
        Attributes:
        -----------
        param point: Describes point of the student
        type point: str max_length=10
    """
    point = models.CharField(blank=True, max_length=10, verbose_name="Оцінка")
