from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from django.views.generic import View
from django.urls import reverse


def get_all_teachers(request):
    context = {'teachers_list': Teacher.objects.all()}
    return render(request, 'teachers_list.html', context)


def delete_all_teachers(request):
    teachers = Teacher.objects.all()
    teachers.delete()
    return redirect('teachers_list')


class TeacherCreate(View):
    def get(self, request):
        form = TeacherForm
        return render(request, 'teacher_create.html', context={'form': form})

    def post(self, request):
        post_form = TeacherForm(request.POST)
        if post_form.is_valid():
            post_form.save()
        return redirect('teachers_list')


def teacher_put(request, id):
    teacher = Teacher.objects.get(pk=id)
    form = TeacherForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            upd_teacher = Teacher.objects.get(pk=id)
            upd_teacher.name = form.cleaned_data["name"]
            upd_teacher.surname = form.cleaned_data["surname"]
            upd_teacher.patronymic = form.cleaned_data["patronymic"]
            upd_teacher.save()
            return HttpResponseRedirect(reverse("teachers_list"))
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "update_teacher_form.html", {'form': form, 'id': id})


def delete_teacher_by_id(request, id):
    context = {}
    obj = get_object_or_404(Teacher, pk=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse("teachers_list"))
    return render(request, "delete_teacher_by_id.html", context)