from django.db import models

POINTS = (
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
    (11, "11"),
    (12, "12"),
    ("зарах.", "зарах."),
)


class Point(models.Model):
    """This class represents a Point.
        Attributes:
        -----------
        param point: Describes point of the student
        type point: str max_length=10
    """
    point = models.CharField(blank=True, max_length=10, verbose_name="Оцінка", choices=POINTS)

    def __str__(self):
        return self.point

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
