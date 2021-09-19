from django.db import models


class Subject(models.Model):
    """This class represents a Subject.
        Attributes:
        -----------
        param subject: Describes subject
        type subject: str max_length=10
    """
    subject = models.CharField(blank=True, max_length=50, verbose_name="Предмет")
    group = models.ForeignKey('score_summary.Group', verbose_name="Група", on_delete=models.CASCADE)
    point = models.OneToOneField('score_summary.Point', null=True, verbose_name="Оцінка", on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"


POINTS = (
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("зарах.", "зарах."),
)


class Point(models.Model):
    """This class represents a Point.
        Attributes:
        -----------
        param point: Describes point of the student
        type point: str max_length=10
    """
    point = models.CharField(null=True, blank=True, max_length=10, verbose_name="Оцінка", choices=POINTS)

    def __str__(self):
        return self.point

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"


class Group(models.Model):
    """This class represents a Group.
        Attributes:
        -----------
        param group: Describes group
        type group: str max_length=20
    """
    group = models.CharField(blank=True, max_length=20, verbose_name="Група")
    curator = models.CharField(null=True, blank=True, max_length=50, verbose_name="Куратор")

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = "Група"
        verbose_name_plural = "Групи"
