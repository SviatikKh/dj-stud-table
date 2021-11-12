from django.forms import modelformset_factory
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


def fill_score_summary(request):
    sc = Scoresummary.objects.all().order_by('-subject')
    scores = {}

    for s in sc:
        if s.point:
            point = s.point.point
        else:
            point = None
        if scores.get(s.student.full_name()):
            scores[s.student.full_name()][s.subject.subject] = point
        else:
            scores[s.student.full_name()] = {s.subject.subject: point}

    context = {'score_summary': scores,
               'students': Student.objects.all(),
               'subjects': Subject.objects.all().order_by('subject')}
    print(f'scores {scores}')
    # save_student_points(request)
    if request.method == "POST":
        print(f'request.POST {request.POST}')

    return render(request, 'score_summary.html', context=context)


def form_score_summary(request):
    form = ScoresummaryForm(data=request.GET)
    if request.method == "POST":
        print(request.POST)
    # ScoresummaryFormset = modelformset_factory(Scoresummary, form=ScoresummaryForm)
    # queryset = Scoresummary.objects.all()
    # # score_summary_formset = modelformset_factory(Scoresummary, form=ScoresummaryForm)
    # formset = ScoresummaryFormset(queryset=queryset)
    # if request.method == "POST":
    #     formset = ScoresummaryFormset(request.POST, queryset=queryset)
    #     if formset.is_valid():
    #         formset.save(commit=False)
    #         return render(request, 'score_summary.html')
    #     else:
    #         formset = ScoresummaryFormset(queryset=Scoresummary.objects.all())
    #     context = {'formset': formset}
    #     return render(request, 'form_score_summary.html', context=context)
    return render(request, 'formform.html', context={"form": form})


def new_score_summary(request):
    context = {'score_summary': Scoresummary.objects.all(),
               'students': Student.objects.all(),
               'subjects': Subject.objects.all()}
    if request.method == "POST":
        form = ScoresummaryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'score_summary.html')
    else:
        return render(request, 'new_score_summary.html', context=context)




# def save_student_points(request):
#     if request.method == "POST":
#         student = request.POST.getlist('student')
#         subject = request.POST.getlist('subject')
#         point = request.POST.getlist('point')
#         print(f'stud {student}')
#         print(f'subject {subject}')
#         print(f"point {point}")






