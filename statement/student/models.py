from django.db import models


class Student(models.Model):
    """This class represents a Student.
           Attributes:
           -----------
           param name: Describes name of the student
           type name: str max_length=20
           param surname: Describes last name of the student
           type surname: str max_length=20
           param patronymic: Describes middle name of the student
           type patronymic: str max_length=20
           param group: Describes group of the student
           type groupc: str max_length=20

       """

    name = models.CharField(blank=True, max_length=20, verbose_name="Ім'я")
    surname = models.CharField(blank=True, max_length=20, verbose_name="Прізвище")
    patronymic = models.CharField(blank=True, max_length=20, verbose_name="По-батькові")
    group = models.CharField(blank=True, max_length=20, verbose_name="Група")

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Student object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
