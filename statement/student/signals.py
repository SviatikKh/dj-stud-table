from django.db.models.signals import post_save
from student.models import Student
from django.dispatch import receiver
from score_summary.models import Scoresummary, Group


@receiver(post_save, sender=Student)
def create_student_data(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(group=instance.group)
        for subject in group.subject.all():
            Scoresummary.objects.create(student=instance, group=instance.group, subject=subject)
