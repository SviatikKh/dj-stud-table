from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from django.views.generic import View
from django.urls import reverse


def get_all_teachers(request):
    teacher1 = Teacher(id=1, name="Марія", surname="Ігонкіна", patronymic="Степанівна")
    teacher1.save()
    teacher2 = Teacher(id=2, name="Микола", surname="Забарко", patronymic="Генадійович")
    teacher2.save()

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
            new_teacher = post_form.save()
            return redirect(new_teacher)
        return render(request, 'teacher_create.html', context={'form': post_form})


def teacher_put(request, id):
    teacher = Teacher.objects.get(pk=id)
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            upd_teacher = Teacher.objects.get(pk=id)
            upd_teacher.update(**form.cleaned_data)
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