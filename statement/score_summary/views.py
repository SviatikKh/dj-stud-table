from django.shortcuts import render, get_object_or_404, redirect

from score_summary.models import Scoresummary, Subject
from student.models import Student
from .forms import ScoresummaryForm

from django import template
register = template.Library()


def show_score_summary(request):
    context = {'score_summary': Scoresummary.objects.all(),
               'students': Student.objects.all(),
               'subjects': Subject.objects.all()}
    return render(request, 'score_summary.html', context=context)


# def subjects_score_summary(request):
#     pass
#
#
# def student_score_summary(request):
#     pass

KEY_MAP = {"Хімія": "chemistry"}


def fill_score_summary(request):
    sc = Scoresummary.objects.all().order_by('-subject')
    scores = {}

    for s in sc:
        if s.point:
            point = s.point.point
        else:
            point = None
        if scores.get(s.student.name):
            scores[s.student.name][s.subject.subject] = point
        else:
            scores[s.student.name] = {s.subject.subject: point}

    context = {'score_summary': scores,
               'students': Student.objects.all(),
               'subjects': Subject.objects.all().order_by('subject')}
    print(scores)
    if request.method == "POST":
        print(request.POST)

    return render(request, 'score_summary.html', context=context)
