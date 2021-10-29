from django.shortcuts import render, get_object_or_404, redirect

from score_summary.models import Scoresummary, Subject
from student.models import Student
# from .forms import ScoresummaryForm


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


def fill_score_summary(request):
    context = {'score_summary': Scoresummary.objects.all(),
               'students': Student.objects.all(),
               'subjects': Subject.objects.all()}
    if request.method == "POST":
        # student_point =
        return redirect('score_summary')
    return render(request, 'score_summary.html', context=context)
