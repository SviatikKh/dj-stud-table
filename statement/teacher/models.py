import logging
from django.db import models

logger = logging.getLogger(__name__)


class Teacher(models.Model):
    """This class represents a Teacher.
        Attributes:
        -----------
        param name: Describes name of the teacher
        type name: str max_length=20
        param surname: Describes last name of the teacher
        type surname: str max_length=20
        param patronymic: Describes middle name of the teacher
        type patronymic: str max_length=20

    """

    name = models.CharField(blank=True, max_length=20, verbose_name="Ім'я")
    surname = models.CharField(blank=True, max_length=20, verbose_name="Прізвище")
    patronymic = models.CharField(blank=True, max_length=20, verbose_name="По-батькові")

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Teacher object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
