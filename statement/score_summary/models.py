from django.db import models


class Scoresummary(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, verbose_name="Студент", null=True)
    group = models.ForeignKey('score_summary.Group', verbose_name="Група", on_delete=models.CASCADE)
    point = models.ForeignKey('score_summary.Point', null=True, blank=True, verbose_name="Оцінка",
                              on_delete=models.SET_NULL)
    subject = models.ForeignKey('score_summary.Subject', null=True, blank=True, max_length=50, verbose_name="Предмет",
                                on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.student.pk} {self.student} {self.group} {self.subject}"


class Subject(models.Model):
    """This class represents a Subject.
        Attributes:
        -----------
        param subject: Describes subject
        type subject: str max_length=10
    """
    name = models.CharField(blank=True, max_length=50, verbose_name="Предмет")
    teacher = models.ForeignKey('teacher.Teacher', null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name="Викладач")
    # semester = models.CharField(blank=True,  max_length=5, verbose_name="Семестр")

    def __str__(self):
        return self.name

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
    ("None", None)
)


class Point(models.Model):
    """This class represents a Point.
        Attributes:
        -----------
        param point: Describes point of the student
        type point: str max_length=10
    """
    value = models.CharField(null=True, blank=True, max_length=10, verbose_name="Оцінка", choices=POINTS)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"


class Group(models.Model):
    """This class represents a Group.
        Attributes:
        -----------
        param name: Describes group
        type name: str max_length=20
    """
    name = models.CharField(blank=True, max_length=20, verbose_name="Група")
    curator = models.CharField(null=True, blank=True, max_length=50, verbose_name="Куратор")
    subject = models.ManyToManyField('score_summary.Subject')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Група"
        verbose_name_plural = "Групи"
