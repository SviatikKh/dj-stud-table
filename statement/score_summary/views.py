from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from score_summary.models import Scoresummary, Subject, Point, Group
from student.models import Student
from .forms import ScoresummaryForm

from django import template

register = template.Library()


def show_score_summary(request):
    context = {'score_summary': Scoresummary.objects.all(),
               'students': Student.objects.all(),
               'subjects': Subject.objects.all()}
    return render(request, 'score_summary.html', context=context)


def fill_score_summary(request):
    sc = Scoresummary.objects.all().order_by('-subject')
    # sc = Scoresummary.objects.filter(group__name=request.POST)
    print('first', request.POST)
    scores = {}
    records_mapping = {}

    for s in sc:
        map_name = f"{s.student.full_name()}_{s.subject.name}"
        records_mapping[map_name] = s
        if s.point:
            point = s.point.value
        else:
            point = None
        if scores.get(s.student.full_name()):
            scores[s.student.full_name()][s.subject.name] = point
        else:
            scores[s.student.full_name()] = {s.subject.name: point}

    context = {'score_summary': scores,
               'students': Student.objects.all(),
               'subjects': Subject.objects.all().order_by('name')}

    if request.method == "POST":
        for key, point in request.POST.items():
            student = records_mapping.get(key)
            if student and point:
                student.point = Point.objects.get(value=point)
                student.save()
                print("record maping", records_mapping.get(key))
        return redirect('score_summary')
    return render(request, 'score_summary.html', context=context)


def group_list(request):
    context = {'group_list': Group.objects.all()}
    return render(request, 'group_list.html', context=context)


def group_detail(request, name):

    sc = Scoresummary.objects.filter(group__name=name)
    scores = {}
    records_mapping = {}

    for s in sc:
        map_name = f"{s.student.full_name()}_{s.subject.name}"
        records_mapping[map_name] = s
        if s.point:
            point = s.point.value
        else:
            point = None
        if scores.get(s.student.full_name()):
            scores[s.student.full_name()][s.subject.name] = point
        else:
            scores[s.student.full_name()] = {s.subject.name: point}

    context = {'score_summary': scores,
               'students': Student.objects.all(),
               'subjects': Subject.objects.all().order_by('name'),
               'group': name}

    if request.method == "POST":
        for key, point in request.POST.items():
            student = records_mapping.get(key)
            if student and point:
                student.point = Point.objects.get(value=point)
                student.save()
                print("record maping", records_mapping.get(key))
        return redirect('score_summary')
    return render(request, 'score_summary.html', context=context)
