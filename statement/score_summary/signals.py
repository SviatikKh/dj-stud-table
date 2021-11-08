from django.db.models.signals import post_save
from student.models import Student
from django.dispatch import receiver
from .models import Scoresummary


@receiver(post_save, sender=Student)
def create_student_data(sender, instance, created, **kwargs):
    if created:
        Scoresummary.objects.create(student=instance)


@receiver(post_save, sender=Student)
def save_student_data(sender, instance, **kwargs):
    instance.student.save()
