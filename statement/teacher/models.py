import logging
from django.db import models, IntegrityError, DataError
Teacherr = logging.getLogger(__name__)


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

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Teacher object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(teacher_id):
        """
        :param teacher_id: SERIAL: the id of a Teacher to be found in the DB
        :return: teacher object or None if a user with such ID does not exist
        """
        try:
            user = Teacher.objects.get(id=teacher_id)
            return user
        except Teacher.DoesNotExist:
            pass

    @staticmethod
    def delete_by_id(teacher_id):
        """
        :param teacher_id: an id of a teacher to be deleted
        :type teacher_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """

        try:
            teacher = Teacher.objects.get(id=teacher_id)
            teacher.delete()
            return True
        except Teacher.DoesNotExist:
            pass
        return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the teacher
        type name: str max_length=20
        param surname: Describes surname of the teacher
        type surname: str max_length=20
        param patronymic: Describes patronymic of the teacher
        type patronymic: str max_length=20
        :return: a new teacher object which is also written into the DB
        """
        teacher = Teacher(name=name, surname=surname, patronymic=patronymic)
        try:
            teacher.save()
            return teacher
        except (IntegrityError, AttributeError, DataError):
            pass

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the teacher
        type name: str max_length=20
        param surname: Describes surname of the teacher
        type surname: str max_length=20
        param patronymic: Describes patronymic of the teacher
        type patronymic: str max_length=20
        :return: a new teacher object which is also written into the DB
        """
        teacher = Teacher(name=name, surname=surname, patronymic=patronymic)
        try:
            teacher.save()
            return teacher
        except (IntegrityError, AttributeError, DataError):
            pass

    def update(self,
               name=None,
               surname=None,
               patronymic=None):
        """
        Updates teacher in the database with the specified parameters.\n
        param name: Describes name of the teacher
        type name: str max_length=20
        param surname: Describes surname of the teacher
        type surname: str max_length=20
        param patronymic: Describes patronymic of the teacher
        type patronymic: str max_length=20
        :return: None
        """

        if name:
            self.name = name
        if surname:
            self.surname = surname
        if patronymic:
            self.patronymic = patronymic
        try:
            from django.db import transaction
            with transaction.atomic():
                self.save()
        except:
            pass

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all teachers
        """
        all_teachers = Teacher.objects.all()
        return all_teachers
