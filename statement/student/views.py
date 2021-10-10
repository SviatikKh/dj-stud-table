from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.views.generic import View
from django.urls import reverse


def get_all_students(request):
    context = {'students_list': Student.objects.all()}
    return render(request, 'students_list.html', context)


def delete_all_students(request):
    students = Student.objects.all()
    students.delete()
    return redirect('students_list')


class StudentCreate(View):
    def get(self, request):
        form = StudentForm
        return render(request, 'student_create.html', context={'form': form})

    def post(self, request):
        post_form = StudentForm(request.POST)
        if post_form.is_valid():
            post_form.save()
        return redirect('students_list')


def student_put(request, id):
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            upd_student = Student.objects.get(pk=id)
            upd_student.name = form.cleaned_data["name"]
            upd_student.surname = form.cleaned_data["surname"]
            upd_student.patronymic = form.cleaned_data["patronymic"]
            upd_student.group = form.cleaned_data["group"]
            upd_student.save()
            return HttpResponseRedirect(reverse("students_list"))
    else:
        form = StudentForm(instance=student)
    return render(request, "update_student_form.html", {'form': form, 'id': id})


def delete_student_by_id(request, id):
    context = {}
    obj = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse("students_list"))
    return render(request, "delete_student_by_id.html", context)
