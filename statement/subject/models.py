from django.db import models


class Subject(models.Model):
    """This class represents a Subject.
        Attributes:
        -----------
        param subject: Describes subject
        type subject: str max_length=10
    """
    subject = models.CharField(blank=True, max_length=50, verbose_name="Предмет")
