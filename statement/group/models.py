from django.db import models


class Group(models.Model):
    """This class represents a Group.
        Attributes:
        -----------
        param group: Describes group
        type group: str max_length=20
    """
    group = models.CharField(blank=True, max_length=20, verbose_name="Група")

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = "Група"
        verbose_name_plural = "Групи"
